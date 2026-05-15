# if, else e elif (condições)
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 13:
    print("Você é adolescente.")
else:
    print("Você é criança.")

# Operadores lógicos: and (e), or (ou), not (não), == (igual), != (diferente)
numero = int(input("Digite um número: "))
if numero > 0 and numero % 2 == 0:
    print("O número é positivo e par.")
elif numero > 0 and numero % 2 != 0:
    print("O número é positivo e ímpar.")
elif numero < 0 and numero % 2 == 0:
    print("O número é negativo e par.")
elif numero < 0 and numero % 2 != 0:
    print("O número é negativo e ímpar.")
else:
    print("O número é zero.")