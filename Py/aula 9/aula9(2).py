from json.tool import main
from unicodedata import name


def contador_letras(Lista_palavras):
    contador=[]
    for x in Lista_palavras:
        quantidade= len(x)
        contador.append(quantidade)
    return contador
if __name__ =='__main__':
    lista=["cachorro","gato"]
    print(contador_letras(lista))

