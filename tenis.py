# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 13:47:22 2022

@author: Fausto Pettinari
"""

import random

print("** Welcome to the Super Tennis Annotator app ** \nType 1 for manual mode or 2 for automatic mode")
mode = int(input("How do you want to use it? "))

while mode!=1 and mode!=2:
    #ciclo indefinido que no termina hasta que se introduzca un modo válido
    print('Invalid mode. Try again.')
    mode = int(input("How do you want to use it? "))

j1, j2 = 0, 0

while j1==j2:
    #ciclo indefinido que no termina hasta que se introduzcan nombres válidos
    print('\nEscriba nombres distintos. Caso contrario se pediran nuevamente.')
    j1, j2 = input("Insert player 1's name: "), input("Insert player 2's name: ")

players = [j1, j2]

def puntos ():
    '''
    Simulacion de un game de un partido de tenis.
    Por cada jugador hay una variable en la que se  guarda su nombre
    y otra en la que se guarda su score. 
    Cada vez que se inserta el nombre de uno de los jugadores, se 
    incrementa el score del mismo. Los puntos incrementan como en 
    un partido normal de tenis, con la siguiente secuencia:
        0 -> 15 -> 30 -> 40 -> Ad
    La evolución del score es mostrada en pantalla durante todo el
    game, y se muestra al final quien es el ganador del partido.
    
    Args:
        j1 (str):
            Almacena el nombre del player 1
        j2 (str):
            Almacena el nombre del player 2

    Returns:
        scr1 (int):
            Almacena el score del player 1
        scr2 (int):
            Almacena el score del player 2
        puntaje (dict):
            Convierte los valores (0, 1, 2, 3, 4) a (0, 15, 30, 40, 'Ad').

    '''
    scr1=0
    scr2=0
    puntaje = {0:0, 1:15, 2:30, 3:40, 4:'Ad'}

    while(True):
        if mode == 1:
            #modo manual
            ws = input('Who scored? ')

        elif mode == 2:
            #modo automático
            ws = random.choice(players)
            print('Who scored?', ws)

        if ws == j1:
            if scr1 < 3:
                scr1 += 1
            elif scr1 == 3:
                if scr2 == 3:
                    scr1 = 4
                elif scr2 == 4:
                    scr2 = scr2 - 1
                else:
                    print(f'{j1} won the game')
                    break
            elif scr1 != 3:
                print(f'{j1} won the game')
                break


        elif ws == j2:
            if scr2 < 3:
                scr2 += 1
            
            elif scr2 == 3:
                if scr1 == 3:
                    scr2 = 4
                elif scr1 == 4:
                    scr1 = scr1 - 1
                else:
                    print(f'{j2} won the game')
                    break
            
            elif scr2  != 3:
                print(f'{j2} won the game')
                break
        
        #impresión del marcador
        print(f'{j1}:', puntaje[scr1])
        print(f'{j2}:', puntaje[scr2])
        
    return 

puntos()