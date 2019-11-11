#!/bin/python3

import math
import os
import random
import re
import sys

CHARS = 26

# Complete the isValid function below.
def isValid(s):
    my_list = list(s) 
    my_freq = {} 

    for item in my_list: 
        if (item in my_freq): 
            my_freq[item] += 1
        else: 
            my_freq[item] = 1

    #convert the dictionary into a list    
    freq_of_freq = list(my_freq.values())

    #convert the list into a set
    freq_of_freq_counts = set(freq_of_freq)
  
    #if the set length is 1 the string is valid
    if(len(freq_of_freq_counts)==1):
        return "YES"
    else:
        # determine the special case. 
        # it's valid if there are only 2 counts, 
        # AND one of them is countOfOtherOne+1:1
        my_freq = {} 

    #build a dictionary
    for item in freq_of_freq: 
        if (item in my_freq): 
            my_freq[item] += 1
        else: 
         my_freq[item] = 1
    #convert the values and keys into lists
    theValues = list(my_freq.values())
    theKeys = list(my_freq.keys())
    
    if(len(theValues) == 2):
        if((theKeys[1] - theKeys[0] <= 1) and (theValues[1] == 1)):
            return "YES"
        else:
            return "NO"
    else:
        return "NO"
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
