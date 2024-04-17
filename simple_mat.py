n1 = int(input("digite um número: "))
n2 = int(input("digite um número: "))

operation = input("Digite qual operação deseja fazer (+, -, *, /): ")

if operation == "+":
    resultado = n1 + n2
elif operation == "-":
    resultado = n1 - n2
elif operation == "*":
    resultado = n1 * n2
elif operation == "/":
    if n2 != 0:
        resultado = n1 / n2
    else:
        resultado = "Não é possível dividir por zero."
else:
    resultado = "Operação inválida."

print("Resultado:", resultado)
