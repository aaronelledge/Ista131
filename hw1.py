
'''
Name: Aaron Elledge
Section Leader: Cedric Vicera
Date: 1/29/20
ISTA HW1 - Python Review + Nested Loops
Collaboration: Ira Sehati
  
'''

# description: this function returns whether the matrix is 
#   diagonal or not
# name: is_diagonal
# type: boolean
# parameter: matrix: lol
# return: return False if it is not a diagonal, True otherwise
def is_diagonal(lol):
    for r in range(len(lol)):
        for c in range(len(lol[r])):
            if r != c and lol[r][c] != 0:
                return False
    return True

# description: this function returns True if all but the lower
#   triangle of the matrix are 0's. 
# name: is_upper_triangular
# type: boolean
# parameter: matrix: lol
# return: True if the lower triangle section of the matrix are 0's,
#   False otherwise
def is_upper_triangular(lol):
    for r in range(len(lol)):
        for c in range(len(lol[r])):
            if r > c and lol[r][c] != 0:
                return False
    return True

# description: this function checks to see if the val is in the matrix
# name: contains
# type: boolean
# parameter: matrix: lol, string: val
# return: True if the "val" is in "lol", False otherwise
def contains(lol, val):
    for r in range(len(lol)):
        for c in range(len(lol[r])):
            if lol[r][c] == val:
                return True
    return False

# description: this function finds the biggest value in the matrix
# name: biggest
# type: int
# parameter: matrix: lol
# return: the biggest value inside the matrix
def biggest(lol):
    largest = lol[0][0];
    for r in range(len(lol)):
        for c in range(len(lol[r])):
            if lol[r][c] > largest:
                largest = lol[r][c]
    return largest

# description: this function returns the location of the biggest value in the matrix
# name: indices_biggest
# type: list
# parameter: matrix: lol
# return: the location at where the biggest value in the matrix is
def indices_biggest(lol):
    if(len(lol[0]) == 1 and len(lol) == 1):
        return [0,0]
    largest = biggest(lol)
    for r in range(len(lol)):
        for c in range(len(lol[r])):
            if lol[r][c] == largest:
                return [r,c];
    return [0,0]

# description: this function returns the second biggest number in the matrix 
# name: second_biggest
# type: int
# parameter: matrix: lol
# return: the second biggest number in the matrix
def second_biggest(lol):
    return sorted(element for row in lol for element in row)[-2] # taken from worksheet

# description: this function returns the location of the seond biggest int inside the
#   matrix
# name: indices_second_biggest
# type: list
# parameter: matrix: lol
# return: the x,y location of the second largest number in the matrix
def indices_second_biggest(lol):
    if(len(lol[0]) == 1 and len(lol) == 1):
        return [0,0]
    loc = second_biggest(lol)
    key = 0
    key = second_biggest(lol)
    for r in range(len(lol)):
        for c in range(len(lol[r])):
            if lol[r][c] == key:
                loc = [r,c]
    return loc

# description: this function gets the places where the "word" occurs in the dictionary
# name: substr_in_values
# type: list
# parameter: dictionary: d, string: word
# return: a list of of the keys where the word occurs
def substr_in_values(d, word):
    out = []
    for key in d:
        for string in d[key]:
            if word.lower() in string.lower():
                if (key not in out):
                    out.append(key)
    out = sorted(out)
    return out

# description: this function returns the numbers in where their indices summed up
#   are divisible by 3
# name: indices_divisible_by_3
# type: list
# parameter: matrix: lol
# return: list of numbers whose indices summed up are divisible by 3
def indices_divisible_by_3(lol):
    out = []
    for r in range(len(lol)):
        for c in range(len(lol[r])):
            if (r+c) % 3 == 0:
                out.append(lol[r][c])
    return out

# description: this function takes a string, changes it into a list of ints, sorts the
#   numbers, puts it back into a list and returns that list
# name: sort_int_string
# type: list
# parameter: string: str
# return: list of ints in order
def sort_int_string(str):
    splt = str.split()
    splt.sort(key=int)#converts whole str to int, for negative numbers
    out = ' '.join(splt)
    return out

# description: this function checks for duplicates inside the matrix
# name: dups_lol
# type: boolean
# parameter: matrix: lol
# return: True if there are duplicates, False otherwise
def dups_lol(lol):
    l = []
    for r in range(len(lol)):
        for c in range(len(lol[r])):
            if(lol[r][c] in l):
                return True
            else:
                l.append(lol[r][c])
    return False

# description: this function checks to see if any values occur twice inside
#   a dictionary
# name: dups_dict
# type: boolean
# parameter: dictionary: d
# return: True if there are duplicates, False othersie
def dups_dict(d):
    keys = []
    for key in d:
        for string in d[key]:
            if string in keys:
                return True
            else:
                keys.append(string)
    return False
