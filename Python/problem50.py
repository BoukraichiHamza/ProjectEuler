#!/usr/bin/env python3

#https://projecteuler.net/problem=50

def sieve(n):
    sieve=[True]*n
    sieve[0]=False
    sieve[1]=False
    sieve[4::2]=[False]*len(sieve[4::2])
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*len(sieve[i*i::2*i])
    return [i for i in range(n) if sieve[i]]


primes1=sieve(500000)   #returns 41538, the index of the last prime lower than 500000
primes=sieve(1000000)

def isPrime(n):
    if n==1:
        return False
    i=2
    while i**2 <= n:
        if n%i==0:
            return False
        i+=1
    return True

def solution():
    mini=500000
    limit1=0
    index=0
    for i in range(41538):
        limit=limit1
        while sum(primes[i:41538-limit])>10**6:
            limit+=1
        limit1=limit
        while not isPrime(sum(primes[i:41538-limit])):
            limit+=1
        if limit < mini:
            mini=limit
            index=i
    return mini,index





    
            
            
    

