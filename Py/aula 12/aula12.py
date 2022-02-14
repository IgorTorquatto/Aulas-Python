lista=[1,2]
try:
   # divisao=10/0
    valor=lista[3]

#except ZeroDivisionError:
   #print("Impossível dividir umm número por 0.")
except IndexError:
    print("A lista não tem nenhum valor nessa posição.")
