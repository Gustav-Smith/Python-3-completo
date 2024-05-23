# nome = "Gustavo Jean"
# resultado = nome[0]
# indice = 1

# while indice < len(nome):
#     letra = nome[indice]
#     resultado += f"*{letra}"
#     indice += 1
    
# print(resultado)

entrada = input('Digite uma string: ')

resultado = entrada[0]
indice = 1

while indice < len(entrada):
    caractere = entrada[indice]
    resultado += f'/{caractere}'
    indice += 1
    
print('Resultado: ', resultado)