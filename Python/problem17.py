#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#https://projecteuler.net/problem=17

numbers = {0:"" ,1: "one", 2: "two", 3: "three", 4: "four", 5: "five",6: "six"
           ,7:"seven", 8:"eight", 9:"nine",10:"ten", 11: "eleven",
           12: "twelve", 13: "thirteen", 14: "fourteen", 15:"fifteen", 
           16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty"
           ,30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",
           90:"ninety",100:"hundred",1000:"onethousand"}



def letters(n):
    a=str(n)
    if len(a)==4:
        chaine=numbers[1000]
        return chaine
    if len(a)==3:
        if (n-int(a[0])*100==0):
            chaine=numbers[int(a[0])]+numbers[100]
            return chaine
        if n-int(a[0])*100>20:
            chaine=numbers[int(a[0])]+numbers[100]+"and"+numbers[int(a[1])*10]+numbers[int(a[2])]
            return chaine
        else:
            chaine=numbers[int(a[0])]+numbers[100]+"and"+numbers[n-int(a[0])*100]
            return chaine
    if len(a)==2:
        if n<20:
            chaine=numbers[n]
            return chaine
        else:
            chaine=numbers[int(a[0])*10]+numbers[int(a[1])]
            return chaine
    if len(a)==1:
        chaine=numbers[int(a[0])]
        return chaine

def solution():
    total=0
    for i in range(1,1001):
        print(letters(i))
        total+=len(letters(i))
    return total
        
print(solution())
    




        
        




    
