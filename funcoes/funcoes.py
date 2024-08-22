def sum(a,b):
    return a + b

c = sum(1,3)
print(c)

#valor padrão caso nada seja passado para imposto
def salario_descontado_imposto(salario, imposto=27.):
    return salario - (salario * imposto * 0.01)
print(salario_descontado_imposto(1000))

#parametros nomeados
print(salario_descontado_imposto(5000, imposto=0.10))


#Unpacking dos argumentos
print("{:.^60}".format("Unpacking dos argumentos"))
def unpacking_experiment(*args):
    arg1 = args[0]
    arg2 = args[1]
    others = args[2:]
    print(arg1)
    print(arg2)
    print(others)
unpacking_experiment(1, 2, 3, 4, 5, 6)

def unpacking_experiment(**kwargs):
    print(kwargs)
unpacking_experiment(named="Test", other="Other")
