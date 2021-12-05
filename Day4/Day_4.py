# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 21:35:25 2021

@author: Youri
"""

def createBingo(lines):
    card = []
    allcards =[]
    bingonumber = list(map(int,lines[0].split(',')))
    
    
    for i in range(2,len(lines)):
        if len(lines[i]) > 1 : 
            lineFiltered = filter(None,lines[i].split(' '))
            intline = list(map(int,lineFiltered))
            card.append(intline)
        else:
            allcards.append(card)
            card =[]
    return(allcards, bingonumber)

def bingoCheater(bingonumber, allcards):
    Winningcard=[]
    WinningNumber = -1
    for number in bingonumber:
        if WinningNumber > 0 :
            break
        for i in range(len(allcards)):
            CurrentCard = allcards[i]
            for j in CurrentCard:
                if number in j:
                    j[j.index(number)] =6969
            for j in CurrentCard:
                if j.count(6969) == len(j):
                    Winningcard = CurrentCard
                    WinningNumber = number
                    break
            [Winningcard, WinningNumber] =vertCheck(CurrentCard,number,Winningcard, WinningNumber)
            if WinningNumber > 0 :
                break
    return(Winningcard, WinningNumber)

def vertCheck(CurrentCard,number,Winningcard, WinningNumber):
    for j in range(len(CurrentCard)):
        checkline=[]  
        for k in range(len(CurrentCard)):
            if CurrentCard[k][j] == 6969:
                checkline.append(6969)
                # print(checkline)
        if len(checkline) == len(CurrentCard):
            Winningcard= CurrentCard
            WinningNumber = number
            break
    return(Winningcard, WinningNumber)
    

def cardScore(card, number):
    Score = 0
    for i in card:
        for j in range(len(card)):
            if i[j] != 6969:
                Score += i[j]
    Score = Score*number
    return(Score)

def badBingoCheater(bingonumber, allcards):
    Winningcard=[]
    WinningNumber = -1
    lastNumber = 0
    lastCard =[]
    wCards = []
    
    for number in bingonumber:
        if WinningNumber > 0 :
            if len(wCards) == len(allcards):
                break
        # else:
        #     lastToWin = i
        for i in range(len(allcards)):
            CurrentCard = allcards[i]
            for j in CurrentCard:
                if number in j:
                    j[j.index(number)] =6969
            for j in CurrentCard:
                if j.count(6969) == len(j):
                    Winningcard = CurrentCard
                    WinningNumber = number
                    if WinningNumber > 0:
                        if i not in wCards:
                            wCards.append(i)
                        if len(wCards) == len(allcards):
                            lastNumber = number
                            lastCard =CurrentCard
                            break
                        WinningNumber = 0
            [Winningcard, WinningNumber] =vertCheck(CurrentCard,number,Winningcard, WinningNumber)
            if WinningNumber > 0 :
                if i not in wCards:
                    wCards.append(i)
                if len(wCards) == len(allcards):
                    lastNumber = number
                    lastCard =CurrentCard
                    break
                WinningNumber = 0
    return(lastNumber, lastCard)

             
            






file = open('input_day4.txt', 'r')
lines = file.read().split('\n')
file.close()
[allcards, bingonumber] =createBingo(lines)
[Winningcard, WinningNumber] = bingoCheater(bingonumber, allcards)
ScoreP1 = cardScore(Winningcard, WinningNumber)
[lastNumber, lastCard] = badBingoCheater(bingonumber, allcards)
ScoreP2 = cardScore(lastCard, lastNumber)