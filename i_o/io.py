# r = leitura, w = escrita (apaga o que tinha antes), b = modo binario, a = edicao, 
# r+ = leitura e escrita
# omitindo o modo o padrao seria r
lista = []
texto = [
    "O primeiro argumento é uma string contendo o nome do arquivo. ",
    "O segundo argumento é outra string, contendo alguns caracteres ",
    "que descrevem o modo como o arquivo será usado. modo pode ser 'r' ",
    "quando o arquivo será apenas lido, 'w' para escrever (se o arquivo ",
    "já existir seu conteúdo prévio será apagado), e 'a' para abrir o arquivo ",
    "para adição; qualquer escrita será adicionada ao final do arquivo. A opção ",
    "'r+' abre o arquivo tanto para leitura como para escrita. O argumento modo ",
    "é opcional, em caso de omissão será assumido 'r'."
]

with open('arquivo.txt','w', encoding="utf-8") as arq:
    for i in texto:
        arq.write(i+"\n")
arq.closed

print('\n\n{:.^60}'.format('Lendo o Arquivo como lista')+"\n")
with open('arquivo.txt', encoding="utf-8") as arq:
    print(list(arq))
arq.closed

print('\n\n{:.^60}'.format('Lendo todo o arquivo ')+'\n')
with open('arquivo.txt', encoding="utf-8") as arq:
    print(arq.read())
arq.closed

print('\n\n{:.^60}'.format('Lendo todo o arquivo limitando caracteres')+'\n')
with open('arquivo.txt', encoding="utf-8") as arq:
    n = 100
    print(arq.read(n))
arq.closed

print('\n\n{:.^60}'.format('Lendo todo o arquivo limitando caracteres')+'\n')
with open('arquivo.txt', encoding="utf-8") as arq:
    n = 100
    print(arq.read(n))
arq.closed

#quando chega ao final retorna string vazia
print('\n\n{:.^60}'.format('Lendo linha por linha')+'\n')
with open('arquivo.txt', encoding="utf-8") as arq:
    linha = True
    while linha:
        linha = arq.readline()
        print(linha)
arq.closed

# com o (a) não deleta e insere no final do arquivo
with open('arquivo.txt','a', encoding="utf-8") as arq:
    arq.write('editei agora')
    arq.write(' editei de novo')
arq.closed