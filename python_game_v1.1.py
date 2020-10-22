#!/bin/python3

"""I.4.a. Zaprogramuj w języku Python (001) grę w zgadywanie liczby z przedziału od 1 do 100.
Program ma za zadanie wylosować liczbę, a użytkownik ma ją zgadnąć. Jeśli użytkownik poda
liczbę mniejszą niż liczba wylosowana, to program wypisuje tekst "za mała liczba", a jeśli
poda większą liczbę, to wypisuje tekst "za duża liczba". Jeśli użytkownik poda wylosowaną
liczbę, to wypisuje tekst „brawo, mój przyjacielu”."""

from random import randrange

random_number = randrange(1,101)
player_number=0
counter=0
#print(random_number)
def funkcja(random_number,player_number,counter):
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
        funkcja(random_number,player_number,counter)

funkcja(random_number, player_number, counter)