# for 
for i in range(5):
    print(f"Iteração {i}")

# while
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1

# break e continue
for i in range(10):
    if i == 3:
        continue  # Pula a iteração quando i é igual a 3
    if i == 7:
        break  # Encerra o loop quando i é igual a 7
    print(f"Valor de i: {i}")

# for each (iterando sobre listas)
tecnologias = ["Python", "JavaScript", "Java", "C#"]
for tech in tecnologias:
    print(f"Aprendendo {tech}")
print("Fim do loop for each.")