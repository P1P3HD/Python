# Definir 3 funciones... Cálculo perímeto, área y volúmen... CUADRILATERO O CUBO

def perimetro(lado_1,lado_2):
    resultado = lado_1*2 + lado_2*2
    return resultado

#def perimetro(ancho,largo):
    return ancho + largo * 2

def area(ancho,largo):
    return ancho * largo

def volumen(ancho,largo,alto):
    resultado = ancho * largo * alto
    return resultado

print(perimetro(2,3))
print(area(2,3))
print(volumen(2,3,4))