
class Calculadora:
    def __init__(self,num1,num2):
        self.valor_a=num1
        self.valor_b=num2
    def soma(self):
        return self.valor_a+self.valor_b
    def sub(self):
        return self.valor_a-self.valor_b
    def multi(self):
        return self.valor_a * self.valor_b
    def div(self):
        return self.valor_a / self.valor_b
calculadora= Calculadora(10,5)
print(calculadora.soma())
print(calculadora.sub())
print(calculadora.multi())
print(calculadora.div())