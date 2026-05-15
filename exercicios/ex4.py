import random

numero_secreto = random.randint(1, 100)
lista = [] # Criando a lista pra armazenar as tentativas

while(True):
    acho = int(input("Insira o seu chute: "))
    lista.append(acho); # Armazena a tentativa
    if acho == numero_secreto: 
        print(f"Numero correto!")
        break;
    elif acho > numero_secreto:
        print(f"{acho} eh maior que o número secreto")
    else:
        print(f"{acho} eh menor que o numero secreto")
print("\nNumeros digitados antes de acertar: \n")
for listagem in lista: # Printagem da lista de numeros 'chutados'
    print(f"{listagem} ")
print("\nFim da lista")