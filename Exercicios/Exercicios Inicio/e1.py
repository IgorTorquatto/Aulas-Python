""" Escreva um Programa que imprime dois numeros de sua escolha
e que depois imprime a soma, a subtração, a multiplicação,
a divisão normal e a divisão inteira,
e o resto da divisão do maior pelo menor
(coloque na mensagem a palavra resto ao invez do símbolo %)

EXEMPLO DE SAÍDA:
>>> 
x = 15 
y = 10
15 + 10 = 25
15 - 10 = 5
15 x 10 = 150
15 / 10 = 1.5
15 // 10 = 1
15 resto 10 = 5
"""
x=5
y=10
print("Soma de",x,"+",y,"=",x+y)
print("Subtração de",x,"-",y,"=",x-y)
print("Multiplicação de",x,"x",y,"=",x*y)
print("Divisão de",y,"/",x,"=",y/x)
print("Divisão Inteira de",y,"por",x,"=",y//x)
print("Resto da divisão de ",y,"por",x,"=",y%x)