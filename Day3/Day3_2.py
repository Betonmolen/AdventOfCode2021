# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 19:18:23 2021

@author: youri
"""
import numpy as np


def bitCounter(line):
    # nbits = len(line[1])
    count = np.zeros(len(line[0]))
    gamma = ''
    epsilon = ''

    for i in range(len(line)):
        for j in range(len(line[i])): 
            number = line[i][j]
            count[j]+= int(number)
    for i in range(len(count)):
        if count[i] > (len(line)/2):
             gamma += str(1)
             epsilon+= str(0)
        else:
            gamma += str(0)
            epsilon += str(1)
    result = int(gamma,2)*int(epsilon,2)
    return(result)
    

def bitCounterPro(line):
    result2 = 0
    for j in line:
        count  = 0
        nRemoved = 0
        for i in range(len(line)):
            # if i >= (len(line) - nRemoved+10):
            #     break 
            # else:
            number = line[i][j]
            count += int(number)
        if count >= (len(line)/2):
            listlength = len(line)
            for i in range(listlength):
                np.disp(listlength)
                if i >= (listlength - nRemoved):
                    break 
                else:
                    if int(line[i][j]) == 1:
                        del line[i]
                        i -= 1 
                        nRemoved+=1
        else:  
            for i in range(listlength):
                if i >= (listlength - nRemoved):
                    break 
                else:
                    if int(listlength) == 0:
                        del line[i]
                        i -= 1 
                  # nRemoved+=1
        # line.remove([])       
    #    f=1
    
    return(result2)

file = open('input_day3.txt', 'r')
line = file.read().split('\n')
file.close()
result = bitCounter(line)
result2 = bitCounterPro(line)
print(result)



