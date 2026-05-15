vida = int(input("Digite a vida inicial do personagem: "))
dano = int(input("Digite o dano por ataque recebido: "))
nAtaq = int(0)
print(f"\nVIDA DO MONSTRO: {vida}")
print(f"DANO POR ATAQUE: {dano} \n")
while vida > 0:
    vida -= dano
    nAtaq += 1
    print(f"ATAQUE {nAtaq} -> VIDA RESTANTE: {vida}")
print(f"MONSTRO DERROTADO EM {nAtaq} ATAQUES!")