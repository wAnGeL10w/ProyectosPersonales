# 1. Importar la biblioteca que acabas de instalar
import mysql.connector

try:
    # 2. Crear la conexión
    #    ¡Asegúrate de poner la NUEVA contraseña que creaste!
    connection = mysql.connector.connect(
        host="localhost",           # Tu servidor (127.0.0.1)
        user="root",                # El usuario que configuraste
        password="AnGe1##1",  # <-- ¡REEMPLAZA ESTO!
        database="myfirstdb"      # La base de datos a la que te conectas
    )

    print("¡Conexión a la base de datos 'myfirstdb' exitosa!")

    # 3. Crear un "cursor"
    # El cursor es como el "brazo" que ejecuta los comandos
    cursor = connection.cursor()

    # 4. Definir la consulta SQL para INSERTAR
    # Usamos %s como marcadores. Es más seguro que poner los
    # valores directamente para evitar inyección SQL.
    sql_query = "INSERT INTO usuarios (nombre, correo) VALUES (%s, %s)"
    
    # 5. Definir los datos que quieres insertar
    datos_nuevos = ("Angel", "angel@ejemplo.com")

    # 6. Ejecutar la consulta con los datos
    cursor.execute(sql_query, datos_nuevos)

    # 7. ¡¡EL PASO MÁS IMPORTANTE!!
    # Para cualquier cambio (INSERT, UPDATE, DELETE),
    # debes hacer "commit" para guardar los cambios en la DB.
    connection.commit()

    print(f"¡Registro insertado con éxito! El ID del nuevo usuario es: {cursor.lastrowid}")

except mysql.connector.Error as err:
    # Manejo de errores
    print(f"Error al conectar o insertar en la base de datos: {err}")

finally:
    # 8. Cerrar todo (siempre)
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexión a MySQL cerrada.")