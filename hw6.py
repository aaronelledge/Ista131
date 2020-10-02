'''
Name: Aaron Elledge
Section Leader: Cedric Vicera
Date: 4/18/20
ISTA 131 HW 6
'''




import pandas as pd
import numpy as np
from datetime import datetime as dt
import matplotlib.pyplot as plt



""" Description: this function returns a list of column names

"""
def get_column_labels():
    return pd.date_range(start='01/01/2018', end='12/31/2018').strftime('%m%d').tolist()


""" Description: reads in the data from the csv and returns it
            as a series

"""
def get_2020():
    data = []
    i = get_column_labels()
    df = pd.read_csv("data_2020.csv", header=None)

    for x in range(len(df)):
        data.append(df.iloc[x,1])
    return pd.Series(data, i[:len(data)])



""" Description: this function takes in a dataframe and returns another
        dataframe that contains two rows for each day from 1979 to 2017.
        A mean row and a two_s row. First one contains the mean, and the
        two_s contains 2 x the standard deviation of the column.

"""
def extract_fig_1_frame(df):
    data = [[], []]
    for i in range(len(df.columns)):
        data[0].append(round(df.iloc[:,i].mean(), 6))
        data[1].append(round(df.iloc[:,i].std() * 2, 6))
    index = ["mean", "two_s"]
    new_df = pd.DataFrame(data, index, df.columns)
    return new_df

""" Description: this function takes a data frame and returns
        a new dataframe with the decadal means 

"""
def extract_fig_2_frame(df):
    index = ["1980s", "1990s", "2000s", "2010s"]
    data = [[], [], [], []]
    for i in range(len(df.columns)):
        data[0].append(round(df.iloc[1:11,i].mean(), 4))
        data[1].append(round(df.iloc[11:21,i].mean(), 4))
        data[2].append(round(df.iloc[21:31,i].mean(), 4))
        data[3].append(round(df.iloc[31:,i].mean(), 4))
    new_df = pd.DataFrame(data, index, df.columns)
    return new_df

""" Description: this function takes a figure 1 frame and another
        dataframe and creates a figure

"""
def make_fig_1(f1, df):
    f1.loc["mean"].plot()
    ax = plt.gca()
    ax.set_ylabel("NW Sea Ice Extent ($10^6# km$^2$)")
    ax.yaxis.label.set_fontsize(24)
    df.loc[2012].plot(linestyle="--")
    xs = np.arange(365)
    yuppers = (f1.loc["mean"]+f1.loc["two_s"]).values.astype(float)
    ylowers = (f1.loc["mean"]-f1.loc["two_s"]).values.astype(float)
    ax.fill_between(xs, yuppers, ylowers, color = "lightgray", label = "$\pm$ 2 std")
    ax.legend()

""" Description: this function takes a figure 2 frame and another
        dataframe and creates a figure

"""
def make_fig_2(f2, df):
    ax = plt.gca()
    ax.set_ylabel("NH Sea Ice Extent ($10^6$ km$^2$)")
    ax.yaxis.label.set_fontsize(24)
    f2.loc["1980s"].plot(linestyle="--")
    f2.loc["1990s"].plot(linestyle="--")
    f2.loc["2000s"].plot(linestyle="--")
    f2.loc["2010s"].plot(linestyle="--")
    xs = np.arange(365)
    ts = get_2020()
    ts.plot(linestyle="-", label = "2020")
    ax.set_xticklabels(["0101", "0220", "0411", "0531", "0720", "0908", "1028", "1217"])
    ax.legend()

""" 
main function
"""
def main():
    df = pd.read_csv("data_79_17.csv", index_col = 0)
    f1 = extract_fig_1_frame(df)
    make_fig_1(f1, df)
    plt.figure()
    f2 = extract_fig_2_frame(df)
    make_fig_2(f2, df)
    plt.show()


if __name__ == "__main__":
    main()