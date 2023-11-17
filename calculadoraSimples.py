

print("Bem vindo a Caalculadora")
num1 = float(input("Insira o valor: "))
num2 = float(input("Insira o valor: "))
operacao = input("Selecione uma operacao(+,-, *,/);  ")

if operacao == "+":
    resultado = num1 + num2
    print("O resultado é:", resultado)

elif operacao == "-":
    resultado = num1 + num2
    print("O resultado é:", resultado)

elif operacao == "*":
    resultado = num1 + num2
    print("O resultado é:", resultado)

elif operacao == "/":
    resultado = num1 + num2
    print("O resultado é:" + resultado)

else: print("Operação inválida")

