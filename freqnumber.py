from ctypes import sizeof
from functools import *
import sys
from tabnanny import check
sys.setrecursionlimit(10000)

cmdIn = sys.argv[1].split(';')

k = cmdIn[0][2:]
inFile = cmdIn[1][6:]
outFile = cmdIn[2][7:]

# printing stuff out to make sure it works
print(k)
print(inFile)
print(outFile)

print()

# List where all characters in file are read
characters = []
f = open(inFile, "r")
while 1:

    # read by character
    char = f.read(1)
    if not char:
        break
    characters.append(char)


f.close()


print(characters)

# Parsing
# loop each digit recursively to see if its a digit by comparing it
# to each of accepted digits array

# if it is a digit we append to an array
# every time we make a new array we copy to a new array every digit

digits = []
accepted_digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']

# Check if element is dogit


def is_digit(v):
    def x(accepted_digits, v): return True if v in accepted_digits else False

    if (x(accepted_digits, v)):
        return True
    else:
        return False


# print(is_digit('1'))

# Run through entire characted array appending and making new list of
# only digits
digits = []
set = ""


def string_add(x, y): return x+y
def string_clear(x): return ""


def confirm_digit():
    return lambda x: string_add(set, x) if is_digit(x) else string_clear(set)


check_append = confirm_digit()


def addString(x, y): return x+y


tmpNumString = ""  # String to hold and add characters to numbers


def append_digits(array, l_index):
    if l_index < 0:
        return
    else:
        append_digits(array, l_index-1)
        y = array[l_index]
        if check_append(y):
            tmpNumSrring = addString(tmpNumString, y)
            print(tmpNumString)
        else:
            tmpNumString = ""


append_digits(characters, len(characters)-1)


# Now we go thrught the array of characters
# If character is digit or if it is . then we keep adding it to string
# If charcater is no digit or . then we hop over it and put string on array


# print(set)
