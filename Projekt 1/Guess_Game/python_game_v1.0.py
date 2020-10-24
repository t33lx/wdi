#!/bin/python3

"""I.4.a. Zaprogramuj w języku Python (001) grę w zgadywanie liczby z przedziału od 1 do 100.
Program ma za zadanie wylosować liczbę, a użytkownik ma ją zgadnąć. Jeśli użytkownik poda
liczbę mniejszą niż liczba wylosowana, to program wypisuje tekst "za mała liczba", a jeśli
poda większą liczbę, to wypisuje tekst "za duża liczba". Jeśli użytkownik poda wylosowaną
liczbę, to wypisuje tekst „brawo, mój przyjacielu”."""

from random import randrange

random_number = randrange(1,101)
player_number=0
print(random_number)
while random_number!=player_number:
    player_number=int(input('Podaj liczbe z przedziału od 1 do 100: '))
    if random_number>player_number and player_number>0:
        print("za mała liczba")
    elif random_number<player_number and player_number<101:
        print("za duża liczba")
    else:
        print("wybrałes liczbe z poza zakresu <1,100>")
else:
    print("Brawo, mój przyjacielu")