#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#https://projecteuler.net/problem=31

def coinsums(coins):
    total=0
    coins1=coins
    for i in range((coins[0]//coins[1])+1):
        coins=coins1
        if len(coins)!=1:
            coins=[coins[0]-i*coins[1]]+coins[2:]
        if coins[0]==0:
            total+=1
            return total
        elif coins[0]!=0 and len(coins)==2:
            coins=[coins[0]]+[2]+[1]
            total+=(coins[0]//coins[1])+1
            return total
        total+=coinsums(coins)
    return total


