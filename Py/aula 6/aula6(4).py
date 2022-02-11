lista_animal=["cachorro","lobo","elefante"]
if "sapo" in lista_animal:
    print("Sapo já existe na lista")
else:
    lista_animal.append("sapo")
    print(lista_animal)
lista_animal.pop()
print(lista_animal)