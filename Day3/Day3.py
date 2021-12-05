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
    line2 = line
    for j in range(len(line[0])):
        count  = 0
        nRemoved = 0
        if j >0:
            try:
                while True:        
                    line2.remove('X')
            except:
                pass
        line = line2
        for i in line:
            number = i[j]
            count += int(number)
        if count >= int(len(line)/2):
            for i in range(int(len((line)))):
                if line[i][j] == '0':
                    line2[i]= 'X'
        elif count < int(len(line)/2):  
            for i in range(int(len(line))):
                if line[i][j] == '1':
                    line2[i] = 'X'
    try:
        while True:        
            line2.remove('X')
    except:
        pass
    Oxygen =line2
    
    return(Oxygen)

def bitCounterProLeast(line):
    result2 = 0
    stopF =0
    line2 = line
    for j in range(len(line[0])):
        if stopF ==1:
            break
        count  = 0
        nRemoved = 0
        if j >0:
            try:
                while True:        
                    line2.remove('X')
            except:
                pass
        line = line2
        for i in line:
            number = i[j]
            count += int(number)
            if stopF ==1:
                break
        if count >= int(len(line)/2):
            for i in range(int(len((line)))):
                if line[i][j] == '1':
                    line2[i]= 'X'
                if line.count('X') == (len(line)-1):
                    stopF = 1
                    break
        elif count < int(len(line)/2):  
            for i in range(int(len(line))):
                if line[i][j] == '0':
                    line2[i] = 'X'
                if line.count('X') == (len(line)-1):
                    stopF = 1
                    break
    try:
        while True:        
            line2.remove('X')
    except:
        pass
    CO2 =line2
    return(CO2)


   
    
    



file = open('input_day3.txt', 'r')
line = file.read().split('\n')
file.close()
result = bitCounter(line)
linedupe = line.copy()
Oxygen = bitCounterPro(line)
CO2 = bitCounterProLeast(linedupe)
result2 = int(Oxygen[0],2) * int(linedupe[0],2)
print(result)
print(result2)


