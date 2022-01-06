idade=int(input("Digite sua idade: "))

if idade>=18:
    print("Você pode tirar a CNH")
    if idade>=21:
        print("Você pode fazer parte do Programa CNH Popular")
else:
    print("Você não pode tirar a CNH")