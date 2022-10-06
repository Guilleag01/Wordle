
import json

def main():
    file = open('listado-general.txt', 'r')
    diccionario = dict()
    listaPalabras = file.read().replace(' ', '').split('\n')
    file.close()
    for palabra in listaPalabras:
        if not len(palabra) in diccionario:
            diccionario[len(palabra)] = list()
        diccionario[len(palabra)].append(palabra)
    jDict = json.dumps(diccionario, indent=4, ensure_ascii=False)
    palabras = open('palabras.json', 'w')
    palabras.write(jDict)
    palabras.close()

    

if __name__ == "__main__":
    main()