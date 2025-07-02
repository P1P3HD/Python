# Función para calcular el Máximo Común Divisor
def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Función para calcular el Mínimo Común Múltiplo
def calcular_mcm(a, b):
    mcd = calcular_mcd(a, b)
    return abs(a * b) // mcd

# Función principal que interactúa con el usuario
def iniciar_programa():
    print("=== Cálculo de MCD y MCM ===")
    try:
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))

        mcd = calcular_mcd(num1, num2)
        mcm = calcular_mcm(num1, num2)

        print(f"El Máximo Común Divisor (MCD) de {num1} y {num2} es: {mcd}")
        print(f"El Mínimo Común Múltiplo (MCM) de {num1} y {num2} es: {mcm}")
    except ValueError:
        print("Error: Debes ingresar números enteros válidos.")

# Llamada a la función principal
iniciar_programa()
