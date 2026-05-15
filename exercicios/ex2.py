# Programa que calcula se o aluno foi aprovado ou nao
nota1 = float(input("Insira a sua primeira nota: "));
nota2 = float(input("Insira a sua segunda nota: "));
notaTrabalho = float(input("Insira a nota do seu trabalho: "));

faltas = int(input("Insira o numero de faltas: "))
# Calculo da media ponderada
media = (3*nota1 + 5*nota2 + 2*notaTrabalho)/10

if faltas > 15:
    print("Aluno reprovado por falta.")
elif media >= 6:
    print("Aluno aprovado.")
else: print("Aluno em prova final.")

print(f"A media do aluno foi igual a {media}.")