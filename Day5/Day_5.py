# -*- coding: utf-8 -*-
import numpy as np

def getCoordinates(lines):
    splitlines = []
    X1 = []
    X2 = []
    Y1 = []
    Y2 = []
    maxX1 = 0
    for i in range(len(lines)):
        splitlines.append(lines[i].split('-'))
        XY1 = (list(map(int,splitlines[i][0].split(','))))
        XY2 = (list(map(int,splitlines[i][1].split(','))))
        X1.append(XY1[0])
        Y1.append(XY1[1])
        X2.append(XY2[0])
        Y2.append(XY2[1])
    return(X1, X2,Y1,Y2)


def ventGrid(lines):
    [X1, X2,Y1,Y2] = getCoordinates(lines)
    maxX2 = np.amax([X1,X2]) 
    maxY2 = np.amax([Y1,Y2])
    Grid = np.zeros((maxX2+1, maxY2+1))
    ventCount=0
    xRangeArray = []
    yRangeArray = []
    for i in range(len(X1)):
        if X1[i] == X2[i]:
            count = 0
            ventCount+=1
            if Y2[i] > Y1[i]:
                yRange = Y2[i]-Y1[i]+1
                yRangeArray.append(yRange)
                for j in range(0,yRange):
                    Grid[X1[i],(Y1[i]+j)]+=1
                    count += 1
            elif Y1[i] > Y2[i]:
                yRange = Y1[i]-Y2[i]+1
                yRangeArray.append(yRange)
                for j in range(0,yRange):
                    Grid[X1[i],(Y2[i]+j)]+=1
                    count += 1
           
        if Y1[i] == Y2[i]:
            count = 0
            ventCount+=1
            if X2[i] > X1[i]:
                xRange = X2[i]-X1[i]+1
                xRangeArray.append(xRange)
                for j in range(0,xRange):
                    Grid[(X1[i]+j,Y1[i])]+=1
                  
                    count += 1
            elif X2[i] < X1[i]:
                xRange = X1[i]-X2[i]+1
                xRangeArray.append(xRange)
                for j in range(0,xRange):
                    Grid[(X2[i]+j,Y1[i])]+=1
                    count += 1
        if Y1[i] != Y2[i] and X1[i] != X2[i]:
            if Y2[i] > Y1[i]:
                yRange = Y2[i]-Y1[i]+1
                yRangeArray.append(yRange)
                for j in range(0,yRange):
                    if X2[i] > X1[i]:
                        Xco = X1[i]+j
                    elif X2[i] < X1[i]:
                        Xco = X1[i]-j
                    Grid[(Xco,(Y1[i]+j))]+=1
                    count += 1
            elif Y1[i] > Y2[i]:
                yRange = Y1[i]-Y2[i]+1
                yRangeArray.append(yRange)
                for j in range(0,yRange):
                    if X2[i] > X1[i]:
                        Xco = X1[i]+j
                    elif X2[i] < X1[i]:
                        Xco = X1[i]-j
                    Grid[(Xco,(Y1[i]-j))]+=1
                    count += 1
                
                
                
        else:
            ventCount+=1
                    
                
    print(np.count_nonzero(Grid >= 2))
    # np.where(>=2,Grid)          
    
    return(Grid, yRangeArray, xRangeArray)
    
    
file = open('input_day5.txt', 'r')
lines = file.read().split('\n')
file.close()
[Grid, yRange,Xrange] = ventGrid(lines)