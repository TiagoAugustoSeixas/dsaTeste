lista1 = ["arroz, frango, tomate, leite"]
print(type(lista1))
print(lista1)

lista2 = ["arroz", "frango", "tomate", "leite"]
print(lista2)

lista3 = [23, 100, "Cientis de dados"]
print(lista3)

item1 = lista3[0]
item2 = lista3[1]
item3 = lista3[2]
print(item1, item2, item3)

print(lista2)
lista2[2] = "chocolate"
print(lista2)

print(lista2)
del lista2[3]
print(lista2)
print("----------------------------------------------------------------------------")

# Listas aninhadas

listas = [[1, 2, 3], [10, 15, 14], [10.1, 8.7, 2.3]]
print(listas)

a = listas[0]
print(a)

b = a[0]
print(b)

print("----------------------------------------------------------------------------")

# OPERAÇÕES COM LISTAS

print(listas)
a = listas[0][0]
print(a)

b = listas[1][2]

print(listas)
print(b)

print(listas)
c = listas[0][2] + 10
print(c)

print(listas)
d = 10
e = d * listas[2][0]
print(e)

print("----------------------------------------------------------------------------")

# CONCATENANDO LISTAS

lista_s1 = [34, 32, 56]
print(lista_s1)
lista_s2 = [21, 90, 51]
print(lista_s2)
lista_total = lista_s1 + lista_s2
print(lista_total)


print(" in mostra o que tem na lista-----------------------")
# OPERADOR IN

lista_teste_op = [100, 2, -5, 3.4]
print(10 in lista_teste_op)
print(100 in lista_teste_op)


print(" len(tamanho da lista) - max, min(maximo de itens, minimo de itens-----------------------")
# Funçõees Built-in(tamanho da lista qutos elementos)

lista_de_numeros = [10, 20, 50, -3.4]
print(len(lista_de_numeros))
print(max(lista_de_numeros))
print(min(lista_de_numeros))


lista_de_caracteres = ["Juliana", "Paulo", "Tiago Seixas"]
print(len(lista_de_caracteres))
print(max(lista_de_caracteres))
print(min(lista_de_caracteres))


print(" append adiciona mais um item aquela lista-----------------------")
# append (adicionar mais um item a lista)

print(lista_de_caracteres)
lista_de_caracteres.append("Carla Carolina")
print(lista_de_caracteres)

print(" count contar quantos elementos tem naquela lista-----------------------")
# count - contar
print(lista_de_caracteres)
print(lista_de_caracteres.count("Carla Carolina"))

print(" Uso uma lista vazia para depois colocar algo dentro-----------------------")
# Uso de lista vazia para depois colocar algo(muito usado)

lista = []
print(lista)
lista.append(10)
print(lista)
lista.append(50)
print(lista)


print(" Copia itens de uma lista cheia para outra vazia-----------------------")
# Copiando itens de uma lista para outra
old_list = [1, 2, 5, 10]
print(old_list)
new_list = []
print(new_list)

for item in old_list:
    new_list.append(item)
print( new_list)


print(" extend adiciona varios itens a minha lista existente-----------------------")
#Extend (adiciona vários itens na minha lista existente)
cidades = ["Recife", "Manaus", "Salvador"]
print(cidades)
cidades.extend(["Fortaleza", "Palmas"])
print(cidades)

print("Index busca algo na minha lista -----------------------")
#index (buscar algo na minha lista)

print(cidades)
print(cidades.index("Salvador"))


print("Insert insere elemntos na posição que eu especificar movendo os itens para o lado -----------------------")
#Insert (vai deslocar os elementos para o lado inserindo o elemento que quero naquela posição especifica)
print(cidades)
cidades.insert(2, 110)
print(cidades)
cidades.remove(110) #Remove um item da lista
print(cidades)
cidades.reverse()
print(cidades)

print("Método sort ordena minha lista -------------------------------------")
#Sort (ordena minha lista)
x = [4, 3, 2, 1]
print(x)
x.sort()
print(x)




