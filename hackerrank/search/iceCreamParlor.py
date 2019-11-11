#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    pricesDictionary = {}

    pricesDictionary[cost[0]] = 1
    for i in range(1, len(cost)):
        if (cost[0] + cost[i]) == money:
            print(1, i + 1)
            return
        pricesDictionary[cost[i]] = i + 1
    
    for i in range(1, len(cost)):
        if (money - cost[i]) in pricesDictionary:
            print (pricesDictionary[cost[i]], pricesDictionary[money - cost[i]])
            return


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
