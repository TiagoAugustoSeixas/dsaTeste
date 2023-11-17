#LOOP

print("Loop For")
print("Criando uma tupla e imprimindo os valores")

tp = (1,2,3,4)
for i in tp:
    print(i)

print("Criando uma lista e imprimindo um dos valores")
ListaDeStrings = ["Data", "Science", "Academy"]
for i in ListaDeStrings:
    print(i)

print("Imprimindo os valores no intervalo entre 0 e 5 (exclisive")
for contador in range(0,5):
    print(contador)

print("Imprimindo numeros pares da lista de numeros")
lista = [1,2,3,4,5,6,7,8,9,10]
for num in lista:
    if num % 2 == 0:
        print(num)

print("Listando os numeros no intervalo entre 0e 101, com incremento em 2")
for i in range (0,101,2):
    print(i)

print("Strings também são sequencias")
for caracter in "Python é uma linguagem de programação divertida":
    print(caracter)

print("LOOP FOR ANINHADO")
lista1 = [0,1,2,3,4]
lista2 = [1,2,3]

for elemento_lista1 in lista1:
    for elemento_lista2 in lista2:
        print(elemento_lista1 * elemento_lista2)
    print("----")

print("Verificando se o numero  47 aparece nas duas listas")

lista1 = [10,16,24,39,47]
lista2 = [32,89,47,76,12]

for elemento_lista1 in lista1:
    for elemento_lista2 in lista2:
        if elemento_lista1 == 47 and elemento_lista2 == 47:
            print("O número 47 foi encontrado nas duas listas")

print("Somar os números pares da primeira lista com os numeros pares da segunda lista")

#USANDO A MESMA LISTA DO EMXEMPLO ANTERIOR
soma = 0
for lista in [lista1, lista2]:
    for num in lista:
        if num % 2 == 0:
            soma += num
print("A soma dos números pares das listas é igual a", soma)



