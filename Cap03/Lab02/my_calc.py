# Python calculadora
def soma(num1, num2):
    total = int(num1) + int(num2)
    return total

def subtracao(num1, num2):
    total = int(num1) - int(num2)
    return total

def multiplicacao(num1, num2):
    total = int(num1) * int(num2)
    return total

def divisao(num1, num2):
    total = int(num1) / int(num2)
    return total

print("1 - Soma.")
print("2 - Subtração.")
print("3 - Multiplicação.")
print("4 - Divisão.")
operacao = int(input("informe a operação (1, 2, 3, 4):"))

if operacao > 4 or operacao < 1 :
    print("Operação inválida.")
else:
    num1 = input("informe o primero numero:")
    num2 = input("informe o segundo numero:")

    if operacao == 1:
        total = soma(num1, num2)
    elif operacao == 2:
        total = subtracao(num1, num2)
    elif operacao == 3:
        total = multiplicacao(num1, num2)
    elif operacao == 4:
        total = divisao(num1, num2)

    print(total)