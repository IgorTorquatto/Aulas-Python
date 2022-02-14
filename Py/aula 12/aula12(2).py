from re import A


while True:
    try:
        x=int(input("Digite um número inteiro qualquer: "))
        print(x)
        break
    except ValueError:
        print("Valor Inválido. Digite um número. ")