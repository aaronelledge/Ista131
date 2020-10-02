'''
Name: Aaron Elledge
Date: 3/4/20
ISTA 131
Lab TA: Cedric Vicera
Collaborators: Ira Sehati, Sam Wallman
'''
import csv
import pandas as pd
import numpy as np
from datetime import datetime

'''
Pulls data from a N_seaice_extent_daily_v3.0.csv file and creates and returns a series object

'''
def get_data():
    fn = 'N_seaice_extent_daily_v3.0.csv'
    df =pd.read_csv(fn, skiprows=2, names=[0, 1, 2, 'Extent'], 
        usecols=[0, 1, 2, 3], parse_dates={'Dates': [0, 1, 2]}, header=None)
    s = df['Extent']
    s.index = df['Dates']    
    return s.reindex(pd.date_range(s.index[0], s.index[-1]))





'''
Function takes a series created get_data and alters it in place 
by filling in the missing data. Replaceing the NaN with the mean of two days.
First loop for every other day missing data, and second for the consecutively
missing data. 
'''
def clean_data(ts):
    for i in range(len(ts)):
        if pd.isnull(ts.iloc[i]):
            ts.iloc[i]=(ts.iloc[i-1] + ts.iloc[i+1]) /2
    for i in range(len(ts)):
        if pd.isnull(ts.iloc[i]):
            ts.iloc[i]=(ts.iloc[i-365] + ts.iloc[i+366]) /2




'''
This function generates and returns a list of strings that will be used 
as column labels in a dataframe

'''

def get_column_labels():
    cols = []
    for m in range(1, 13):
        for d in range(1, 32):
            if m==2 and d > 28:
                continue
            if m in [4, 6, 9, 11] and d > 30:
                continue
            cols.append(str(m).zfill(2) + str(d).zfill(2))
    return cols        


'''
This function takes the cleaned Series as its arguement and creates
and returns a new Dataframe. The dataframe will have the yeras from 1979 to 2019
as row labels and the strings from get_column_label as column labels.

'''

def extract_df(s):
    index = list(range(1979, 2020))
    columns = get_column_labels()
    df = pd.DataFrame(index=index, columns=columns, dtype = np.float64)
    for yr in df.index:
        for mmdd in df.columns:
            dt = datetime(yr, int(mmdd[:2]), int(mmdd[2:]))
            df.loc[yr, mmdd] = s.loc[dt]
    return df        




'''
This function takes the cleaned Series as its argument and returns
a Series containing the data for 2020

'''

def extract_2020(s):
    return s.loc[datetime(2020, 1, 1):]




'''
Uses the above functions to read in the data we want, clean it, and store it
'''

def main():
    s = get_data()
    clean_data(s)
    extract_df(s).to_csv('data_79_19.csv')
    extract_2020(s).to_csv('data_2020.csv', header = False)


if __name__ == "__main__":
    main()
