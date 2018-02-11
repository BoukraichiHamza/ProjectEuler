#!/usr/bin/env python3

#https://projecteuler.net/problem=37

def isPrime2(n):
    if n==1:
        return False
    i=2
    while i**2 <= n:
        if n%i==0:
            return False
        i+=1
    return True
    
def truncatable(n):
    m=str(n)
    if '0' in m: 
        return False
    if '2' in m[1:]:
        return False
    if m[0]=='1' or m[len(m)-1]=='1':
        return False
    for i in range(2,5):
        if str(2*i) in m:
            return False
    if '5' in m[1:]:
        return False 
    for i in range(len(m)):
        if not isPrime2(int(m[i:])) or not isPrime2(int(m[:len(m)-i])):
            return False
    return True

def solution():
    total=0
    i=10
    somme=0
    while (total<11):
        if (truncatable(i)==True):
            somme+=i
            print(i)
            total+=1
        i+=1
    return somme

print(solution())
        
    

    

