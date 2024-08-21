#não vai somar
fact = "The Moon has no atmosphere."
fact + "No sound can be heard on the Moon."
print(fact)

# certo a se fazer
fact = "The Moon has no atmosphere."
two_facts = fact + "No sound can be heard on the Moon."
print(two_facts)

#simplificando
fact = "The Moon has no atmosphere."
fact += "No sound can be heard on the Moon."
print(fact)

#.title retorna com iniciais maiusculas
print("temperatures and facts about the moon".title())

#dividir caracteres, sem argumentos separa por espaço
temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures.split()
print(temperatures_list)

#dividir no final de cada linha
temperatures = "Daylight: 260 F\n Nighttime: -280 F"
temperatures_list = temperatures.split('\n')
print(temperatures_list)

#verificar se uma cadeia de caracteres existe em outra
print("Moon" in "This text will describe facts and challenges with space travel")
print("Moon" in "This text will describe facts about the Moon")

#recuperar a posição que a palavra Moon está, se retorna -1 é por que não existe
#se existir retorna a posição que a palavra começa
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("daytime"))

#Outra maneira de pesquisar conteúdo é usar o método .count(), 
# que retorna o número total de ocorrências de uma determinada 
# palavra em uma cadeia de caracteres:
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.count("Mars"))
print(temperatures.count("Moon"))


#converter para tudo minusculo
print("The Moon And The Earth".lower())

#converter para tudo maiusculo
print("The Moon And The Earth".upper())

#separar para pegar o número
temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts)
print(parts[1])

# se não for regular pode usar para encontrar número
mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)


#trocar palavras
print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))


moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts))
print("The highest temperature on Mars is about 30 C".split())


# usar a mesma variavel mais de uma vez
mass_percentage = "1/6"
print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage))

#outra forma de printar
print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth.")


print('{:<60}'.format('\n\nalinhado a esquerda'))
print('{:>60}'.format('alinhado a direita'))
print('{:^60}'.format('centralizando em 60 posições'))
print('{:.^60}'.format('centralizando ao alterar caractere em 60 posições'))