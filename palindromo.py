# Solicita ao usuário que forneça uma palavra
palavra = input("Digite uma palavra: ")

# Remove espaços em branco e converte a palavra para minúsculas
palavra = palavra.replace(" ", "").lower()

# Inverte a palavra
palavra_invertida = palavra[::-1]

# Verifica se a palavra original é igual à palavra invertida
if palavra == palavra_invertida:
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo.")
