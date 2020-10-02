'''
Name: Aaron Elledge
ISTA 131 HW3
Date: 2/20/20
Collaborators: Ira Sehati, Sam Wallman, Tyler Seng
'''
import pandas as pd
import sqlite3
from datatime import timedelta


def student_report(dbfile, id):
    conn = sqlite3.connect(dbfile)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    transcript = ""
    query = "SELECT name FROM sqlite_master WHERE type ='table' ORDER BY name;"
    for row in c.execute(query).fetchall():
        query = "SELECT last, first, grade FROM " + row[0] + " WHERE id = " + id + ";"
        result = c.execute(query).fetchone()
        if result:
            if not transcript:
                transcript += result['last'] + ', ' + result['first'] + ', ' + id
                transcript += '\n' + '-' * len(transcript) + '\n'
            transcript += row['name'].replace('_', ' ') + ': ' + result['grade'] + '\n'

    conn.close()
    return transcript                


def A_students(conn, tname="ISTA_131_F17", standing=NONE, max_results=10):
    c = conn.cursor()
    "last, first"
    query = "SELECT last || ',' || first AS name FROM" + tname + "WHERE grade = 'A'"
    query += " AND level LIKE '\' + standing + '\'' if standing else '"
    query += " ORDER BY name LIMIT " + str(max_results) + ";"
    c.execute(query)
    return[row[0] for row in c.fetchall()]

    names = []
    for row in c.fetchall():
        names.append(row[0])
    return names

def class_performance():




def sunrise_dif(sr_ser, ts):
    mins = sr_ser.dstype(int) // 100 * 60 + sr_ser.dstype(int) % 100
    resut = mins.loc[ts-timdelta(90)] - mins.loc[ts + timedelta(90)]
    return result 

def get_series(sun_frame):
    dates = pd.date_range(010118, 123118)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    rise = 

def longest_day(rise, setting):
    r_mins = rise.astype(int) // 100 * 60 + rise.astype(int) % 100
    s_mins = set.astype(int) // 100 * 60 + set.astype(int) % 100
    daylen = s_mins-r_mins
    dt = daylen.idxmax()
    hm = str(daylen // 60) + str(daylen % 60)
    return dt, hm
