# Usamos el ciclo FOR para recorrer elementos de un grupo de datos
juegos = ["Dota 2","MK","Street Fighter","Counter Strike","7DaystoDie"]
numeros = [10,20,30,40]

for juego in juegos: 
    print(juego) 

for numero in numeros:
    resultado = numero * numero
    print(f"El resultado de multiplicar {numero} * {numero} = {resultado}")