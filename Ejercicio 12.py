barra_nueva= 3.49
numero_barras_pasadas = int(input("Introduzca las barras no vendidas: "))
descuento = 0.6
descuento_barra = (barra_nueva * descuento)
barra_pasada = barra_nueva - (barra_nueva * descuento)

print("precio de una barra fresca es de : ")
print(barra_nueva, "€")
print("descuento por no ser una barra fresca es de : ")
print(descuento_barra, "€")
print("precio de una barra no fresca es de : ")
print(barra_pasada, "€")
print("Gananacia total es de : ")
print(barra_pasada * numero_barras_pasadas, "€")
