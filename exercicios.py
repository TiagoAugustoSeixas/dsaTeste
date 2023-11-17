# TUPLAS - É USÁDO QUANDO NÃO QUERO QUE MINHA ESTRUTURA DE DADOS NÃO SEJA ALTERADO

print(" Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros)

print("Exercício 2 - Crie uma lista de 5 objetos e imprima na tela")
objetos = ['objeto1', 'objeto2', 'objeto3', 'objeto4', 'objeto5']
print(objetos)

print("Exercício 3 - Crie duas strings e concatene as duas em uma terceira string")
nome1 = "string1"
nome2 = "string"
nome3 = nome1 +  nome2
print(nome3)


print(" 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do \n",
    "objeto tupla para verificar quantas vezes o número 4 aparece na tupla")
tupla1 = (1, 2, 2, 3, 4, 4, 4, 5)
print(tupla1.count(4))

print(" Exercício 5 - Crie um dicionário vazio e imprima na tela")
dicionarioVazio = []
print(dicionarioVazio)

print(" Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela")
dicionario1 = {"chave1":1, "chave2":2, "chave3":3}
print(dicionario1)

print(" Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela")
dicionario1["chave4"]=4
print(dicionario1)

print(" Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. \n",
       " Um dos valores deve ser uma lista de 2 elementos numéricos. \n",
       " Imprima o dicionário na tela.")
dicionario2 = {"elemento1":1, "elemento2":2, "elemnto3":[1, 2]}
print(dicionario2)

print(    " Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, \n",
    " o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e \n",
    " o quarto elemento um valor do tipo float.\n",
    " Imprima a lista.")
lista = ["letra", (1, 2), {"teste1":3, "teste2":4}, 2.45]
print(lista)



