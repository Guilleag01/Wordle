import json
import random
from socket import gaierror
import termcolor

def main():
    palabras = dict()
    palabras = loadPalabras("palabras.json")
    print("Introduce el número de letras que quieres: ")
    numLetras = input()
    palabra = "vaduz" # random.choice(palabras[numLetras])
    tablero = generateTablero(int(numLetras))
    play(tablero, palabra, palabras)
    # printTablero(tablero, palabra)

def loadPalabras(filename):
    file = open(filename, 'r')
    jFile = json.load(file)
    file.close()
    return jFile

def generateTablero(tamano):
    return [[" " for i in range(tamano) ] for j in range(tamano + 1)]

def play(tablero, palabra, diccionario):
    guesses = 0
    for i in range(len(palabra) + 1):
        printTablero(tablero, palabra)
        correctWord = False
        while(not correctWord):
            print("Introduce una palabra: ", end="")
            guess = input()
            correctWord = checkPalabra(guess, palabra, diccionario)
        
        for i in range(len(guess)):
            tablero[guesses][i] = guess[i]

        guesses += 1

def printTablero(tablero, palabra):
    print("┌", end="")
    for i in range(len(palabra)):
        print("─", end="")
    print("┐")
    
    for i in range(len(palabra)):
        print("│", end="")
        for j in range(len(palabra)):
            if tablero[i][j] == palabra[j]:
                termcolor.cprint(tablero[i][j], 'white', 'on_green', end="")
            elif palabra[:j].count(tablero[i][j]) == tablero[i][:j].count(tablero[i][j]):
                termcolor.cprint(tablero[i][j], 'white','on_yellow', end="")
            else:
                print(tablero[i][j], end="")
        print("│")
    
    print("└", end="")
    for i in range(len(palabra)):
        print("─", end="")
    print("┘")

    print(palabra)
    
def checkPalabra(guess, palabra, diccionario):
    if not (len(guess) == len(palabra)):
        print("Longitud incorrecta")
        return False
    if not guess in diccionario[str(len(palabra))]:
        print("Esa palabra no existe")
        return False 
    return True

if __name__ == "__main__":
    main()