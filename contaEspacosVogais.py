frase = str(input('Digite uma frase: ')).lower()
vogais = int(0)
vogais += frase.count("a")
vogais += frase.count("e")
vogais += frase.count("i")
vogais += frase.count("o")
vogais += frase.count("u")


print('Tem {} espaços.'.format(frase.count(" ")))
print('Tem {} vogais na frase.'.format(vogais))


