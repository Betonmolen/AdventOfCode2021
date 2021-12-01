# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def countDepthIncrease(line):
    
    result = 0 
    for i in range(1,len(line)):
        if  int(line[i]) > int(line[i-1]):
            result+=1
    return result
        
def countDepthIncreaseNoise(line):
    
    result = 0
    size = len(line)
    line =list(map(int,line))
    for i in range(1,size):
        if  sum(line[i:i+3]) > sum(line[(i-1):(i+2)]):
            result+=1
    return result




file = open('input_day1.txt', 'r')
line = file.read().split('\n')
file.close()
(answerP1) = countDepthIncrease(line)
(answerP2) = countDepthIncreaseNoise(line)