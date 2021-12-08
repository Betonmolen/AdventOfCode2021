# -*- coding: utf-8 -*-


def lanternFish(lines):
    numberString =lines[0]
    splitnumbers = numberString.split(',')
    fishies = list(map(int,(splitnumbers)))
    for i in range(256):
        for j in range(len(fishies)):
            if fishies[j] == 0:
                fishies[j] = 6
                fishies.append(8)
            else:
                fishies[j] = fishies[j] -1
                
    result = len(fishies)
    
    return (result)

def lanternFish2(lines):
    numberString =lines[0]
    splitnumbers = numberString.split(',')
    fishies = list(map(int,(splitnumbers)))
    
    Bucket = [0] * 9
    
    for i in fishies:
        Bucket[i] += 1
        
    for i in range(256): 
        newfish = Bucket[0]
        for i in range(1,9):
            Bucket[i-1] = Bucket[i]
        Bucket[6] += newfish
        Bucket[8] = newfish 
    
    
    
    
  

                
    result = sum(fishies)
    
    return (result2)





file = open('input_day6.txt', 'r')
lines = file.read().split('\n')
file.close()
result = lanternFish(lines)
result2 = lanternFish2(lines)

