#!/bin/python3

"""I.4.a. Zaprogramuj w języku Python (001) grę w zgadywanie liczby z przedziału od 1 do 100.
Program ma za zadanie wylosować liczbę, a użytkownik ma ją zgadnąć. Jeśli użytkownik poda
liczbę mniejszą niż liczba wylosowana, to program wypisuje tekst "za mała liczba", a jeśli
poda większą liczbę, to wypisuje tekst "za duża liczba". Jeśli użytkownik poda wylosowaną
liczbę, to wypisuje tekst „brawo, mój przyjacielu”."""

from random import randrange

random_number = randrange(1,101)
player_number=0

def funkcja(random_number,player_number):
    player_number=int(input('Podaj liczbe z przedziału od 1 do 100: '))
    while player_number<=100 and player_number>=1:
        if random_number > player_number:
            print('za mała liczba')
            player_number=int(input('Podaj liczbe z przedziału od 1 do 100: '))
        elif random_number < player_number:
            print('za duża liczba')
            player_number=int(input('Podaj liczbe z przedziału od 1 do 100: '))
        else:
            print('brawo, mój przyjacielu')
            break
    else:
        print('Podałeś liczbę, która nie jest z przedziału <1,100>!')
        funkcja(random_number,player_number)

funkcja(random_number, player_number)