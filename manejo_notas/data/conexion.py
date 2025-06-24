import mysql.connector

# CTRL + SHIFT + P para cambiar el interpete de python, y ejecutar "pip3 install mysql-connector"

conexion = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    database='gestion_notas'
)

cursor = conexion.cursor()

def ejecutar_consulta(consulta):
    cursor.execute('SELECT * FROM asignaturas')
    resultado = cursor.fetchall()
    return resultado