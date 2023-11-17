#OPERADORES RELACIONAIS

print("COndicional if e else e elif")
if 5 > 2:
    print("Verdadeiro")
else:
    print("Falso")

dia = "Terça"
if dia == "Segunda":
    print("Hoje fará sol")
else:
    print("Hoje vai chover")

if dia == "Segunda":
    print("Hoje fará sol")
elif dia == "Terça":
    print("Hoje vai chover")
else:
    print("Sem previsão de tempo para o dia selecionado")

    # Relacionais
print("RELACIONAIS")
print(6>3)
print(3>7)
print(4<8)
print(4<=4)

if 5 == 5:
    print("Testando Python")

print("CONDICIONAIS ANINHADOS")

idade = 18
if idade > 17:
    print("Você pode dirigir")

Nome = "Bob"
if idade > 13:
    if Nome == "Bob" :
        print("Ok Bob, você está autorizado a entrar!")
    else:
        print("Desculp, mas você não pode entrar")

idade = 13
Nome = "Bob"
if idade >= 13 and Nome == "Bob":
    print("Ok Bob, você está autorizado a entrar!")

idade = 12
Nome = "Bob"
if (idade >= 13) and (Nome == "Bob"):  #No python não é obrigatório usar parenteses, mas por questão de limpesa do código é bom usar
    print("Ok Bob, você está autorizado a entrar!")

#PLACEHOLDER

print("PlaceHolders")
disciplina = "Data Science"
nota_final = 90
semestre = 2

if disciplina == "Data Science" and nota_final >= 80 and semestre != 1:
    print("Você foi aprovado em %s com média final %r !" %(disciplina, nota_final))
else:
    print("Lamento acho que você precisa estudar mais")

