#!/bin/python3

"""I.4.a. Zaprogramuj w języku Python (001) grę w zgadywanie liczby z przedziału od 1 do 100.
Program ma za zadanie wylosować liczbę, a użytkownik ma ją zgadnąć. Jeśli użytkownik poda
liczbę mniejszą niż liczba wylosowana, to program wypisuje tekst "za mała liczba", a jeśli
poda większą liczbę, to wypisuje tekst "za duża liczba". Jeśli użytkownik poda wylosowaną
liczbę, to wypisuje tekst „brawo, mój przyjacielu”."""

import json
import webbrowser
from bdb import bar
from random import randrange
from time import sleep
from os import system
from art import *
from progress.bar import Bar


def clear(): 
    system("cls")

def loading_en():
    tprint("Guess a number")
    bar = Bar('Loading', fill='#', suffix='%(percent)d%%')
    for i in range(100):
        sleep(0.01)
        bar.next()
    bar.finish()

def loading_pl():
    tprint("Zgadnij liczbe")
    bar = Bar('Ładowanie', fill='#', suffix='%(percent)d%%')
    for i in range(100):
        sleep(0.01)
        bar.next()
    bar.finish()

def menu_pl():
    clear()
    tprint("Gra Python")
    print("[1] Nowa Gra")
    print("[2] Ranking")
    print("[3] Autorzy")
    print("[4] Easter Egg")
    print("[5] Wyjście")
    sel_menu=input("Wybrane: ")
    sel_menu=int(sel_menu)
    if(sel_menu==1):
        clear()
        maingame_pl()
    elif(sel_menu==2):
        clear()
        leaderboard_pl()
    elif(sel_menu==3):
        credit_pl()
    elif(sel_menu==4):
        clear()
        egg=input("Napisz coś: ")
        egg=str(egg)
        tprint(egg,"rand")
        print("Proszę czekać...")
        sleep(4)
        menu_pl()
    elif(sel_menu==5):
        quit
    else:
        clear()
        print("Zły numer! \nProszę wybrać z przedziału <1,5>")
        menu_pl()

def menu_en():
    clear()
    tprint("Python Game")
    print("[1] New Game")
    print("[2] Leaderboards")
    print("[3] Credits")
    print("[4] Easter Egg")
    print("[5] Quit")
    sel_menu=input("Selected: ")
    sel_menu=int(sel_menu)
    if(sel_menu==1):
        clear()
        maingame_en()
    elif(sel_menu==2):
        clear()
        leaderboard_en()
    elif(sel_menu==3):
        credit_en()
    elif(sel_menu==4):
        clear()
        egg=input("Write something: ")
        egg=str(egg)
        tprint(egg,"rand")
        print("Please wait...")
        sleep(4)
        menu_en()
    elif(sel_menu==5):
        quit
    else:
        clear()
        print("Wrong number! \nPlease select <1,5>")
        menu_en()

def leaderboard_en():
    clear()
    with open('ranks.txt') as f:
        data=json.load(f)
        tprint("Leaderboard:")
        for i in data:
            print(i[0], i[1])
        x=input("\nPress [1] to quit: ")
        x=int(x)
        if x==1:
            menu_en()
        else:
            leaderboard_en()

def leaderboard_pl():
    clear()
    with open('ranks.txt') as f:
        data=json.load(f)
        tprint("Ranking:")
        for i in data:
            print(i[0], i[1])
        x=input("\nNaciśnij [1] aby wyjść: ")
        x=int(x)
        if x==1:
            menu_pl()
        else:
            leaderboard_pl()

def credit_en():
        clear()
        print("======================================================")
        print("Project authors: \n")
        sleep(1)
        print("Daniel Piekarczyk")
        print("*")
        sleep(1)
        print("Jakub Skupień")
        print("*")
        sleep(1)
        print("Adam Ostrowski")
        print("*")
        print("======================================================")
        print("[1] Link")
        print("[2] Quit")
        sel_credits=input("Selected: ")
        sel_credits=int(sel_credits)

        if sel_credits==1:
            webbrowser.open("https://github.com/t33lx/wdi/tree/master/Projekt%201")
            menu_en()
        elif sel_credits==2:
            menu_en()
        else:
            clear()
            print("Wrong number! \nPlease select <1,2>")
            credit_en()

def credit_pl():
        clear()
        print("======================================================")
        print("Autorzy projektu: \n")
        sleep(1)
        print("Daniel Piekarczyk")
        print("*")
        sleep(1)
        print("Jakub Skupień")
        print("*")
        sleep(1)
        print("Adam Ostrowski")
        print("*")
        print("======================================================")
        print("[1] Link")
        print("[2] Wyjście")
        sel_credits=input("Wybrane: ")
        sel_credits=int(sel_credits)

        if sel_credits==1:
            webbrowser.open("https://github.com/t33lx/wdi/tree/master/Projekt%201")
            menu_pl()
        elif sel_credits==2:
            menu_pl()
        else:
            clear()
            print("Zły numer! \nProszę wybrać z przedziału <1,2>")
            credit_pl()

def language():
    clear()
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
        language()

def menu_game_pl(nick, counter):
    print("======================================================")
    print("[1] Nowa Gra")
    print("[2] Zapisz wynik")
    print("[3] Ranking")
    print("[4] Wyjście")
    sel_game=input("Wybrane: ")
    sel_game=int(sel_game)
    if sel_game==1:
        maingame_pl()
    elif sel_game==2:
        bestscores={}
        with open('ranks.txt') as f:
            data=json.load(f)
        bestscores.update(data)
        bestscores.update({nick : counter})
        bestscores=sorted(bestscores.items(), key=lambda x:x[1])
        with open('ranks.txt', 'w') as f:
            json.dump(bestscores,f)
        print("Zapisywanie...")
        sleep(2)
        clear()
        menu_game_pl(nick, counter)
    elif sel_game==3:
        leaderboard_pl()
    elif sel_game==4:
        menu_pl()
    else:
        clear()
        print("Zły numer! \nProszę wybrać z przedziału <1,4>")
        menu_game_pl(nick, counter)

def menu_game_en(nick, counter):
    print("======================================================")
    print("[1] New Game")
    print("[2] Save Score")
    print("[3] Leaderboard")
    print("[4] Quit")
    sel_game=input("Selected: ")
    sel_game=int(sel_game)
    if sel_game==1:
        maingame_en()
    elif sel_game==2:
        bestscores={}
        with open('ranks.txt') as f:
            data=json.load(f)
        bestscores.update(data)
        bestscores.update({nick : counter})
        bestscores=sorted(bestscores.items(), key=lambda x:x[1])
        with open('ranks.txt', 'w') as f:
            json.dump(bestscores,f)
        print("Saving...")
        sleep(2)
        clear()
        menu_game_en(nick, counter)
    elif sel_game==3:
        leaderboard_en()
    elif sel_game==4:
        menu_en()
    else:
        clear()
        print("Wrong number! \nPlease select <1,4>")
        menu_game_en(nick, counter)


def maingame_pl():
    loading_pl()
    nick=input("Podaj nick: ")
    random_number = randrange(1,101)
    player_number=0
    counter=0

    #print(random_number)
    player_number=int(input('Podaj liczbe z przedziału od 1 do 100: '))
    while player_number!=random_number:
        if random_number > player_number and player_number>=0:
            print('Za mała liczba')
            counter+=1
            player_number=int(input('Podaj liczbe z przedziału od 1 do 100: '))
        elif random_number < player_number and player_number<=100:
            print('Za duża liczba')
            counter+=1
            player_number=int(input('Podaj liczbe z przedziału od 1 do 100: '))
        else:
            print('Podałeś liczbę, która nie jest z przedziału <1,100>!')
            counter+=1
            player_number=int(input('Podaj liczbe z przedziału od 1 do 100: '))
                
    else:
        clear()
        counter+=1
        print('Brawo '+ nick +', zgadłeś za ' + str(counter) + " razem!")
        menu_game_pl(nick, counter)

def maingame_en():
    loading_en()
    nick=input("Enter the nickname: ")
    random_number = randrange(1,101)
    player_number=0
    counter=0
    #print(random_number)
    player_number=int(input('Enter a number from 1 to 100: '))
    while player_number!=random_number:
        if random_number > player_number and player_number>=0:
            print('The number is too small')
            counter+=1
            player_number=int(input('Enter a number from 1 to 100: '))
        elif random_number < player_number and player_number<=100:
            print('The number is too large')
            counter+=1
            player_number=int(input('Enter a number from 1 to 100: '))
        else:
            print('You entered a number that is not in the range of <1,100>!')
            counter+=1
            player_number=int(input('Enter a number from 1 to 100: '))
                
    else:
        clear()
        counter+=1
        print('Congrats '+ nick +', You guessed a number in ' + str(counter) + ' tries!')
        menu_game_en(nick, counter)        



language()
