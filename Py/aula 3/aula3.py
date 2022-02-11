a=int(input("Digite um valor:"))
b=int(input("Digite um valor:"))
c=int(input("Digite um valor:"))

if a>b and a>c:
    print("Maior valor é {}".format(a))
elif b>a and b>c:
    print("Maior valor é {}".format(b))
else:
    print("Maior valor é {}".format(c))