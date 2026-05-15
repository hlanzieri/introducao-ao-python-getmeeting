# Recebe os valores marca, distancia percorrida, litros consumidos e calcula o consumo medio 
marca = str(input("Insira a marca do seu carro: "))
dist = float(input("Insira a distancia percorrida: "))
litros = float(input("Insira o consumo do carro em litros: "))
consumo = dist/litros;
# Printa todas as informacoes
print(f"O carro da marca {marca}, percorreu {dist} km(s) e consumiu {litros} litro(s), com um consumo de {consumo} km/l")

# Verificando o tipo de cada variável
print("Tipo da variavel marca" + type(marca))
print("Tipo da variavel dist" + type(dist))
print("Tipo da variavel litros" + type(litros))
print("Tipo da variavel consumo" + type(consumo))