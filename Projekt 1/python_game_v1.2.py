#!/bin/python3

"""I.4.a. Zaprogramuj w języku Python (001) grę w zgadywanie liczby z przedziału od 1 do 100.
Program ma za zadanie wylosować liczbę, a użytkownik ma ją zgadnąć. Jeśli użytkownik poda
liczbę mniejszą niż liczba wylosowana, to program wypisuje tekst "za mała liczba", a jeśli
poda większą liczbę, to wypisuje tekst "za duża liczba". Jeśli użytkownik poda wylosowaną
liczbę, to wypisuje tekst „brawo, mój przyjacielu”."""

from random import randrange
from art import *
from os import *
from time import sleep

def clear(): 
    if name == 'nt': 
        _ = system('cls') 

def menu_pl():
    tprint("Python Game")
    print("[1] Nowa Gra")
    print("[2] Ranking")
    print("[4] Autorzy")
    print("[5] Easter Egg")
    print("[6] Wyjście")

def menu_en():
    tprint("Python Game")
    print("[1] New Game")
    print("[2] Ranking")
    print("[4] Credits")
    print("[5] Easter Egg")
    print("[6] Quit")
    sel_menu=input("Selected: ")
    sel_menu=int(sel_menu)
    if(sel_menu==1):
        clear()
        maingame()
    elif(sel_menu==2):
        print("in progress...")
    elif(sel_menu==3):
        


def language():
    print("Language: ")
    print("[1] English")
    print("[2] Polski")
    sel_lang=input("Selected: ")
    sel_lang=int(sel_lang)
    if sel_lang==1:
        clear()
        menu_en()
    elif sel_lang==2:
        clear()
        menu_pl()
    else:
        clear()
        print("Wrong number! \nPlease select [1] or [2]")
        language()

random_number = randrange(1,101)
player_number=0
counter=0

#print(random_number)
def maingame(random_number,player_number,counter):
    player_number=int(input('Podaj liczbe z przedziału od 1 do 100: '))
    while player_number<=100 and player_number>=1:
        if random_number > player_number:
            print('za mała liczba')
            counter+=1
            player_number=int(input('Podaj liczbe z przedziału od 1 do 100: '))
        elif random_number < player_number:
            print('za duża liczba')
            counter+=1
            player_number=int(input('Podaj liczbe z przedziału od 1 do 100: '))
        else:
            counter+=1
            print('brawo, mój przyjacielu, zgadłeś za ' + str(counter) + " razem!")
            break
    else:
        print('Podałeś liczbę, która nie jest z przedziału <1,100>!')
        counter+=1
        maingame(random_number,player_number,counter)

language()
maingame(random_number, player_number, counter)