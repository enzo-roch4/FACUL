with open("./exemplo.txt") as file:
    for line in file:
        print(line)

with open ("exemplo.txt", "r+") as f:
    texto = f.read()
    f.write("\nTeste nova linha")

arquivo = open("./exemplo.txt")
texto = arquivo.read()

conta_letras = {}
conta_palavras = {}
for linha in conta_palavras:
    palavras = linha.split()
    for palavra in palavras:
        conta_palavras[palavra] = conta_palavras.get(palavra, 0) + 1
        for letra in palavras:
            conta_letras[letra] = conta_letras.get(letra, 0) + 1

from pprint import pprint

pprint(conta_letras)
pprint(conta_palavras)

max_palavra = [None, 0]
for char, count in conta_palavras.items():
    if max_palavra[1] < count:
        max_palavra = [char, count]

max_char = [None, 0]
for char, count in conta_letras.items():
    if max_char[1] < count:
        max_char = [char, count]

with open("result.txt", "w") as f:
    f.write(f"Palavra mais frequente: {max_palavra[0]}\n")
    f.write(f"Frequência: {max_palavra[1]}\n")
    f.write("\n" + "=" * 50 + "\n")
    f.write(f"Letra mais frequente: {max_char[0]}\n")
    f.write(f"Frequência: {max_char[1]}\n")
