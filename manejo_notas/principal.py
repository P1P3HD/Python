lista_asignaturas = ['Biología','Química','Física']

print(len(lista_asignaturas))
print(len("Hola"))

def mostrar_listado_asignatura():
    print()
    print('Lista de Asignaturas')
    print('====================')
    contador = 0
    for asignatura in sorted(lista_asignaturas):
        contador += 1
        print(f'{contador}- {asignatura}')

def buscar_asignatura():
    busqueda = input('Ingrese asignatura a buscar: ')
    for asignatura in lista_asignaturas:
        if busqueda.lower() in asignatura.lower():
            return asignatura

def agregar_asignatura():
    mostrar_listado_asignatura()
    nueva_asignatura = input('Ingrese nueva asignatura: ')
    lista_asignaturas.append(nueva_asignatura.title())
    mostrar_listado_asignatura()

def actualizar_asignatura():
    mostrar_listado_asignatura()
    busqueda = input('Ingresa asignatura a buscar: ')
    for i in range(len(lista_asignaturas)):
        if busqueda.lower() in lista_asignaturas[i].lower():
            nuevo_dato = input(f'Ingrese nuevo nombre para asignatura {lista_asignaturas[i]}: ')
            lista_asignaturas[i] = nuevo_dato
    mostrar_listado_asignatura()

actualizar_asignatura()
