#!/usr/bin/env python3

#https://projecteuler.net/problem=19

Months={1:'Janvier',2:'Fevrier',3:'Mars',4:'Avril',5:'Mai',6:'Juin',7:'Juillet',
        8:'Aout',9:'Septembre',10:'Octobre',11:'Novembre',12:'Decembre'}

Jours={1:'Lundi',2:'Mardi',3:'Mercredi',4:'Jeudi',5:'Vendredi',6:'Samedi',0:'Dimanche'}

Days={'Janvier':31,'Fevrier':28,'Mars':31,'Avril':30,'Mai':31,'Juin':30,'Juillet':31,
        'Aout':31,'Septembre':30,'Octobre':31,'Novembre':30,'Decembre':31}

def moisprochain(jour,mois,annee):
    mois=mois%12
    if mois==0:
        mois=12
    if mois==2:
        if annee%400==0:         
            days=Days[Months[mois]]+1
            return (jour+days)%7
        elif annee%4==0 and annee%100!=0:
            days=Days[Months[mois]]+1
            return (jour+days)%7         
        else:
            days=Days[Months[mois]]
            return (jour+days)%7
    else:
        days=Days[Months[mois]]
        return (jour+days)%7
        

def firstday(day,année):
    jour,mois=day,1
    while mois <= 12:
        jour=moisprochain(jour,mois,année)
        mois+=1
    return jour

firstday1901=firstday(1,1900)

def solution():
    année=1901
    total=0
    mois=1
    day=firstday(1,1900)
    while année <= 2000:
        jour=day
        print(Jours[jour],année)
        mois=1
        while mois <= 12:
            jour=moisprochain(jour,mois,année)
            if Jours[jour]=='Dimanche':
                total+=1
            mois+=1
        day=firstday(day,année)
        année+=1
    return total
        

        
        
    
        
        
    




    
    
    
    



    

