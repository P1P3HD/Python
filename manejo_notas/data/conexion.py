import mysql.connector

conexion = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    database='gestion_notas'
)

cursor = conexion.cursor()

cursor.execute('SELECT * FROM docentes')
resultado = cursor.fetchall()
print(resultado) 

# CTRL + SHIFT + P para cambiar el interpete de python, y ejecutar "pip3 install mysql-connector"