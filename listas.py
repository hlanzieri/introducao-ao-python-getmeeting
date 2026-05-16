# Listas em Python 
frutas = ["maçã", "banana", "laranja"]

frutas.append("pera") # pera é adicionada ao final da lista
print(frutas)  # Imprime ["maçã", "banana", "laranja", "pera"]
frutas.insert(1, "uva") # uva é inserida na posição 1 (entre maçã e banana)
print(frutas)  # Imprime ["maçã", "uva", "banana", "laranja", "pera"]
frutas.remove("banana") # remove a primeira ocorrência de "banana" na lista
print(frutas)  # Imprime ["maçã", "uva", "laranja", "pera"]
fruta_removida = frutas.pop(2) # remove e retorna o elemento na posição 2 (laranja)
print(frutas)  # Imprime ["maçã", "uva", "pera"]
print(fruta_removida)  # Imprime "laranja"
frutas.sort() # ordena a lista em ordem alfabética
print(frutas)  # Imprime ["maçã", "pera", "uva"]
frutas.reverse() # inverte a ordem da lista
print(frutas)  # Imprime ["uva", "pera", "maçã"]