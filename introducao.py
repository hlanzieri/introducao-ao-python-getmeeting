# Printando uma mensagem de boas-vindas
print("Ambiente Python configurado com sucesso!")

# Varivel sem tipagem explícita
variavel = "Olá, mundo!"
print(variavel)

# Listas
tecnologias = ["Python", "TypeScript", "React"]

# Loop para iterar sobre a lista de tecnologias
for tech in tecnologias:
    print(f"-> Estudando {tech}")

# Printando letra a letra
for letra in "Python":
    print(letra)

# Comandos len (tamanho da lista) e append (adicionar elementos na lista) para listas
print(f"Quantidade de tecnologias: {len(tecnologias)}")
tecnologias.append("Node.js")
print(f"Lista atualizada: {tecnologias}")

# Tuplas (imutáveis) -> utilizadas em situações onde os dados não devem ser alterados (dados cadastrais, de configurações, etc.)
tupla_exemplo = (1, 'dois', 3.0, (4, 5)) # identação de parenteses

# Input para receber dados do usuário
nome = input("Digite seu nome: ")
print(f"Olá, {nome}! Bem-vindo ao mundo da programação!") 
# f -> format que permite inserir variáveis dentro de strings ou " " + variavel " "

# Dicionários (chave-valor)
funcionario = {
    "nome": "João",
    "idade": 30,
    "cargo": "Desenvolvedor"
}

for chave in funcionario:
    print(f"{chave}: {funcionario[chave]}")

# Manipulação do dicionário
funcionario["salario"] = 5000
funcionario["nome"] = "Humberto"

# Operadores aritmeticos diferentes "exoticos"
a = 10
b = 3
print("Divisão Inteira:", a // b)   # 3
print("Exponenciação:", a ** b)   # 1000