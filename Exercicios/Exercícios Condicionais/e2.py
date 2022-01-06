"""
Faça um programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.

Informe ao usuário a quantidades de latas de tinta
a serem compradas e o preço total.
"""
print("------LOJA DE TINTAS-------")
tamanho=float(input("Insira o tamaho em m2 da área a ser pintada: "))
qtd_tinta=tamanho/3
print("Você precisará de: ",qtd_tinta," Litros para pintar a área desejada.")
preco=(80*qtd_tinta)/18
print("O preço será de : ",preco," RS.")
latas=qtd_tinta/18
print("Será preciso ",latas,"Latas de tinta para preencher a área.")
