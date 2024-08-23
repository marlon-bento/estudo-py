def func(f):
    def teste(*args):
        print("testando",args)
    def wrapper(x,y):
        print("Iniciada")
        print("Finalizada")
        teste(x)
        
    return teste
#mesmo que fazer f1 = func(f1)
@func
def f1(x,y):
    print(f"O valor de x é = {x}")
@func
def f2():
    print("Função f2() chamada")

f1(5,6)

def divisao_inteligente(func):
    def interior(x,y):
        print("Será feita uma divisão de {0} por {1}".format(x,y))
        if y == 0:
            print("Impossível dividir")
            return
        return func(x,y)
    return interior
@divisao_inteligente
def divisao(x,y):
    return x / y        
divisao(3,3)
# Será feita uma divisão de 3 por 3
# 1.0
divisao(3,0)
# Será feita uma divisão de 3 por 0
# Impossível dividir