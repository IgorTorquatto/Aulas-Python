if __name__=='__main__':
    class Calculadora:
        def __init__(self):
            pass
        def soma(self,valor_a,valor_b):
            return valor_a+valor_b
        def sub(self,valor_a,valor_b):
            return valor_a-valor_b
        def multi(self,valor_a,valor_b):
            return valor_a*valor_b
        def div(self,valor_a,valor_b):
            return valor_a/valor_b
    calculadora= Calculadora()
    print(calculadora.soma(10,2))
    print(calculadora.sub(3,4))
    print(calculadora.multi(7,5))
    print(calculadora.div(100,10))