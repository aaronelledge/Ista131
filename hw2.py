'''
Name: Aaron Elledge
Section Leader: Cedric Vicera
Date: 2/10/20
ISTA 131 HW 2
'''


""" Description: this function tells the user whether the input number is a power of 2 or not
"""
import numpy as np
import sqlite3
import csv
import os

def is_power_of_2(num):

    if (num == 1 or num == 2):
        return True

    while (num > 0):
        if num == 2:
            return True
        num=num/2

    return False


""" Description: this function figures out whether all the numbers in the matrix are divisible by 2 or not
"""
def all_power_of_2(m):
    for arr in m:
        for val in arr:
            if not is_power_of_2(val):
                return False
    return True



""" Description: this function returns the first number in the matrix that is divisible by the given number
"""
def first_divisible(m, num=2):

    rows = m.shape[0]
    cols = m.shape[1]
    for x in range(0, rows):
        for y in range(0, cols):
            if m[x,y] % num == 0:
                return [x,y]
    return None


""" Description: this function makes a list containing all the numbers that are multiple of 4 in the matrix
"""
def multiples_of_4(m):
    out = []
    rows = m.shape[0]
    cols = m.shape[1]
    for x in range(0, rows):
        for y in range(0, cols):
            if (x+y) % 4 == 0:
                out.append(m[x,y])
    return out


""" Description: this function takes a dictionary and maps the values to a numpy matrix and returns it
""" 
def to_array(d):
    out = []
    for key in d:
        out.append(sorted(d[key]))

    return np.array(out)



""" Description: this function creates a table within the csvfile
"""
def to_table(csvFile, sqlFile, t = "new1"):    


    conn = sqlite3.connect(sqlFile)
    c = conn.cursor()
    l = [] #list with the file info inside
    names = []


    with open(csvFile) as f:
        reader = csv.reader(f)
        for row in reader:
            names.append(', '.join(row))
            l.append(row)

    q = "CREATE TABLE IF NOT EXISTS " + t + " ("+l[0][0]+" TEXT PRIMARY KEY, "
    
    temp = 1
    colNames = "("+ l[0][0] + ","

    while temp < len(l[0]):
        q+= str(l[0][temp]) + " TEXT, "
        colNames += str(l[0][temp]) + ","
        temp+=1

    q = q[0:-2] + ")"

    c.execute(q) #table created

    colNames = colNames[0:-2] + ")" # list of all the column names


    q = "" #querey
    q = ("INSERT INTO " + t + " (" + (names[0]) + ") VALUES(")
    temp = 0

    while temp < len(l[0]):
         q += "?,"
         temp+=1
    q = q[0:-1] + ")"


    temp = 1
    while temp < len(l):
        ins = (str(l[temp][0]), str(l[temp][1]),  str(l[temp][2]), str(l[temp][3]))
        c.execute(q, (ins))
        temp+=1

    conn.commit()

    


def to_csv(sql_fname, table_name, csv_fname ="data.csv"):
    csv_fp = open(csv_fname, 'w', newline = '')
    writer = csv.writer(csv_fp)
    
    conn = sqlite3.connect(sql_fname)
    conn.row_factory = sqlite.rowc = conn.cursor()

    c.execute('SELECT * FROM' + table_name + ';')
    columns = [tup[0] for tup in c.descripton]
    writer.writerow(columns)
    for row in c.fetchall(): 
        writer.writerow(list(row))
    csv_fp.close()
    conn.commit()    

""" Description: this function connects to a file of students and creates a list with their last, first names that match
    the given grade 
"""
def get_students(conn, tbl, grd):
    c = conn.cursor()
    c.execute('SELECT last || ',' || first AS name FROM '  + tbl + " WHERE grade = '" + grd + "' ORDER BY name;")
    result = []
    for row in c.fetchall():
       result.append(row[0])
    return result    




