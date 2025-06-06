while True:
    try:
        num = int(input("Ingresa un número: "))
        break
    except ValueError:
        print("Ingrese nuevamente los datos.")

