lista = [1, 20, 7, 50, 10]
print("tamanho da lista: ", len(lista))
print("mostrar da posição 1 até a 3: ", lista[1:3])
print("ultimo elemento: ", lista[-1])

#lista vazia é false
listaVazia = []
if listaVazia:
    print("não vai executar")
else:
    print("lista vazia")

for i in lista:
    print(i)