import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sortli = sorted(ar)
    newli = list(set(ar))
    flag = False
    pair = 0
    temp = 0
    li = []
    # print(newli)
    # print(sortli)
    for i in range(len(newli)):
        if newli[i] in sortli:
            li.append(sortli.count(newli[i]))
    # print(li)        
    def check():
        nonlocal pair
        for index,j in enumerate(newli):
            temp = j
            if temp >= 2:
                temp -= 2
                flag = True
                pair += 1
                newli.insert(index,temp)
    if flag:
        check()
    if temp == 0:
        check()
    return pair

# if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

n = int(input())

arr = list(input().split(' '))
ar = [int(i) for i in arr]
result = sockMerchant(n, ar)
print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
