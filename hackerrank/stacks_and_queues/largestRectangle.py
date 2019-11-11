#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(buildings):
    # This function calulates maximum  
    # rectangular area under given  
    # histogram with n bars 
  
    # Create an empty stack. The stack  
    # holds indexes of histogram[] list.  
    # The bars stored in the stack are 
    # always in increasing order of  
    # their heights. 
    stack = list() 
  
    maxArea = 0 # Initialize max area 
  
    # Run through all bars of 
    # given histogram 
    index = 0
    while index < len(buildings): 
          
        # If this bar is higher  
        # than the bar on top 
        # stack, push it to stack 
  
        if (not stack) or (buildings[stack[-1]] <= buildings[index]): 
            stack.append(index) 
            index += 1
  
        # If this bar is lower than top of stack, 
        # then calculate area of rectangle with  
        # stack top as the smallest (or minimum 
        # height) bar.'i' is 'right index' for  
        # the top and element before top in stack 
        # is 'left index' 
        else: 
            # pop the top 
            topOfStack = stack.pop() 
  
            # Calculate the area with  
            # histogram[top_of_stack] stack 
            # as smallest bar 
            area = (buildings[topOfStack] * 
                   ((index - stack[-1] - 1)  
                   if stack else index)) 
  
            # update max area, if needed 
            maxArea = max(maxArea, area) 
  
    # Now pop the remaining bars from  
    # stack and calculate area with  
    # every popped bar as the smallest bar 
    while stack: 
          
        # pop the top 
        topOfStack = stack.pop() 
  
        # Calculate the area with  
        # histogram[top_of_stack]  
        # stack as smallest bar 
        area = (buildings[topOfStack] * 
              ((index - stack[-1] - 1)  
                if stack else index)) 
  
        # update max area, if needed 
        maxArea = max(maxArea, area) 
  
    # Return maximum area under  
    # the given histogram 
    return maxArea 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
