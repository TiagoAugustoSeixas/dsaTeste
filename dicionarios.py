print("DICIONARIOS")
print("dict - trabalhando com chave e valor__________________")

estudantes_dict = {"Pedro": 24, "Ana": 22, "Ronaldo": 26, "Janaina": 25}
print(estudantes_dict)
print(estudantes_dict["Pedro"])  # Busco por exemplo pela idade porque esta relacionado a Pedro

print("Adicionando no dicionário")
estudantes_dict["Marcelo"] = 23
print(estudantes_dict)

print("Limpando o dicionário")
estudantes_dict.clear()
print(estudantes_dict)

print("Deletando o dicionário")
del estudantes_dict

estudantes = {"Pedro": 24, "Ana": 22, "Ronaldo": 26, "Janaina": 25}
print(estudantes)

print("Usando método Built-in")
print("len - tamanho do dicionário")
print(len(estudantes))

print("Retornando só as chves ou só os valores ou os dois")
print(estudantes.keys())
print(estudantes.values())
print(estudantes.items())

print("update juntando dois dicionários")
print(estudantes)
estudantes2 = {"Camila": 27, "Adriana": 28, "Roberta": 26}
print(estudantes2)
estudantes.update(estudantes2)
print(estudantes)

print("Criando dicionário vazio e adicionando elementos")
dic1 = {}
print(dic1)
dic1["chave_um"] = 2
print(dic1)

print("Adicionando valor do dicionário em dicinário vazio e atribuindo a outra variavel de acordo com o que eu queira"
      "tanto chave como valor")
teste1 = {"oi": 2, "amor": 3, "olhos": 4}
a = teste1["oi"]
b = teste1["amor"]
c = teste1["olhos"]
print(a, b, c)

teste2 = {}
teste2["chave_1"] = 10
teste2["chave_2"] = 20
teste2["chave_3"] = 30
print(teste2)

a = teste2["chave_1"]
b = teste2["chave_2"]
c = teste2["chave_3"]
print(a, b, c)

print("Dicionário de listas")
dict3 = {"chave1": 1230, "chave2": [22, 453, 73.4], "chave3": ["picanha", "fraldinha", "alcatra"]}
print(dict3)
print(dict3["chave1"])

print("Acessando um item da lista, dentro do dicionario")
print(dict3["chave3"][0].upper()) # Colocando o elemento selecionado dentro da lista em maiusculo

# Acessando um item da lista dentro do dicionário
var1 = dict3["chave2"][0] - 2
print(var1)

# Duas operações do mesmo comando, para atualizar um item dentro da lista
dict3["chave2"][0] -= 2
print(dict3["chave2"][0]) # ele já substitui o valor dentro da lista


