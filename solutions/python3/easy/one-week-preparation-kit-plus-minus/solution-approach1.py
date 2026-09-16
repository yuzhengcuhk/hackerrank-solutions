# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem?isFullScreen=true
# Problem     Plus Minus
# Difficulty  Easy
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-16, 04:51 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n = len(arr)
    pos, neg, zero = 0, 0, 0
    
    for x in arr:
        if x>0:
            pos += 1
        elif x<0:
            neg += 1
        else:
            zero += 1
    for c in (pos, neg, zero):
        print(f"{c/n:.6f}")
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
