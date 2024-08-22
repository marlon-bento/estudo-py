import json
texto = [
    "O primeiro argumento é uma string contendo o nome do arquivo. ",
    "O segundo argumento é outra string, contendo alguns caracteres ",
    "que descrevem o modo como o arquivo será usado. modo pode ser 'r' ",
    "quando o arquivo será apenas lido, 'w' para escrever (se o arquivo ",
    "já existir seu conteúdo prévio será apagado), e 'a' para abrir o arquivo "
    
]
#salva o json em um arquivo
with open('save_json.txt','w', encoding="utf-8") as arq:
    json.dump(texto, arq)
arq.closed

with open('save_json.txt','r', encoding="utf-8") as arq:

    desserializacao = json.load(arq)
    print(desserializacao)

print('\n\n{:.^60}'.format('diretamente'))
print(json.dumps(texto))
print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))

print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))