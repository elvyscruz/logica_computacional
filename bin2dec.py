# Programa que convierte de decimal a bin

binario = input("Digite el numero binario -> ")
decimal = 0

for digito in binario:
    decimal = decimal * 2 + int(digito)
print(decimal)
