salario = int(input('Salario? '))
imposto = 27.

while imposto > 0:
    imposto = input('Imposto ou (0) para sair: ')
    if not imposto:imposto = 27.
    else:
        imposto = float(imposto)
        print("Valor real: {0}".format(salario - (salario *(imposto * 0.01))))


print("{:.^60}".format("percorrer lista"))
lista = [1, 20, 7, 50, 10]
for i in lista:
    print(i)

# print de 0 a 4 range(0, 5)
print("{:.^60}".format("for com range"))
n = 5
for i in range(n):
    print(i)

#enumerate
print("{:.^60}".format("enumeração"))
impostos = ['MEI', 'Simples']
for i, imposto in enumerate(impostos):
    print(i, imposto)