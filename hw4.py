'''
Name: Aaron Elledge
Date: 2/25/2020
ISTA 131
Section Leader: Cedric Vicera
Collaborators: Ira Sehati, Sam Wallman
'''
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime

'''
This function takes a csv filename as an argument and returns a dataframe
'''

def csv_to_dataframe(csv_file):
    return pd.read_csv(csv_file, decimal=',', index_col=0)

'''
This function takes a countries dataframe from the past function, and 
replaces it with title case version and the trailing whitespace stripped

'''

def format_df(df):
    df.index = [idx.strip() for idx in df.index]
    df['Region'] = [region.strip().title() for region in df['Region']]




'''
Function finds a countries growth rate by subtracting the deathrate
from the birthrate

'''


def growth_rate(df):
    df['Growth Rate'] = df['Birthrate'] - df['Deathrate']


'''
This function takes an initial population and a growth rate in 1000's of individuals
per year and returns the number of years it will take for the population of the country 
to go extinct if the growth rate doesn't change

'''


def dod(p,r):
    num_yrs = 0
    while p > 2:
        p = p + p * r / 1000
        num_yrs += 1
    return num_yrs


'''
This function takes a formatted data frame that has growth rate column and adds
a column labeled 'Years to Extinction'. Replace the NaN in the new column
for every country that has a negative growth rate with the number of years 
until pop. is extinct

'''

    
def years_to_extinction(df):
    df['Years to Extinction'] = np.nan
    for country in df.index:
        if df.loc[country, 'Growth Rate'] < 0:
            df.loc[country, 'Years to Extinction'] = dod(df.loc[country, 'Population'], df.loc[country, 'Growth Rate'])
   

 

'''
This function takes a Dataframe that has a Years to Extinction column and returns
a series whose labels are the countries with negative growth rates with 
values that are numbers of years until they're dead in order from first
to last death

def dying_countries(df):
    return df[df['Years to Extinction']>0]['Years to Extinction'].sort_values()

'''



def dying_countries(df):
    d = []
    c = []
    for country in df.index:
        if df.loc[country, 'Years to Extinction'] > 0 :
            d.append(df.loc[country, 'Years to Extinction'])
            c.append(country)
    return pd.Series(d, index=c).sort_values()        

'''
This function takes a connection object and a table name with default
ISTA_131_F17 and returns a dictionary mapping the grades capitilized to
the exact % of the class that got the grade

'''



def class_performance(conn, tbname="ISTA_131_F17"):
    c = conn.cursor()
    c.execute('SELECT UPPER(grade), 100.0 * COUNT(*) / (SELECT COUNT(*) FROM ' + tbname + ') FROM ' + tbname + ' GROUP BY grade;')
    performance = {}
    for row in c.fetchall():
        performance[row[0]] = round(row[1], 1)
    return performance   



'''
This function takes conn object and two table names and returns a sorted list of the 
last names of the students that performed better in the second table
than they did in the first

'''


def improved(conn, t1name, t2name):
    c = conn.cursor()
    c.execute('SELECT ' + t1name + '.last AS name FROM ' + 
        t1name + ' INNER JOIN ' + t2name + ' ON ' + 
        t1name + '.email=' + t2name + '.email ' + 
        'WHERE ' + t1name + '.grade < ' + t2name + '.grade ORDER BY name;')
    

    improvement  = []
    for row in c.fetchall():
        improvement.append(row[0])
    return improvement        



'''
Creates a frame from csv file countries_of_the_world, formats the frame,
adds Growth Rate and Years to extinction columns and prints the top 5 dying countries.
'''

def main(): 
    first = csv_to_dataframe('countries_of_the_world.csv')
    format_df(first)
    growth_rate(first)
    years_to_extinction(first)

    second = dying_countries(first)

    for i in range(5):
        print('{}: {} Years to Extinction'.format(second.index[i], str(round(second[i], 0)))) 

if __name__ == '__main__':
    main()




