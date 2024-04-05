import mysql.connector

# Establecer los parámetros de conexión
config = {
    'user': '',
    'password': '',
    'host': '',
    'database': '',
}

try:
    conexion = mysql.connector.connect(**config)
    print('Conexion exitosa')
except mysql.connector.Error as e:
    print(f"Error al conectar a la base de datos: {e}")
cursor = conexion.cursor()

def verDB(id):
    try:
        cursor.execute("SELECT precio FROM productos WHERE id=%s", (id,))
    except mysql.connector.Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        conexion.close()
        return  # Exit the function on error
    # Obtener los resultados
    fila = cursor.fetchall()
    return fila

def editarDB(id, precio):
    # Editar el registro
    try:
        cursor.execute(f"""UPDATE productos SET precio=%s WHERE ID=%s""",
                       (precio, id))
    except mysql.connector.Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        conexion.close()
        return  # Exit the function on error
    conexion.commit()
    print('Precio modificado')

def verInflation():
    try:
        cursor.execute("SELECT * FROM inflation")
    except mysql.connector.Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        conexion.close()
        return  # Exit the function on error
    # Obtener los resultados
    fila = cursor.fetchall()
    return fila
    conexion.commit()
    print("Registro editado correctamente!")  # Print success message after commit


def editarDBinflation(total, daily, monthly, month):
    try:
        conexion = mysql.connector.connect(**config)
        print('Conexion exitosa')
    except mysql.connector.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return  # Exit the function on error

    cursor = conexion.cursor()

    try:
        cursor.execute("""UPDATE inflation SET TOTALSUM=%s, DAILY=%s, MONTHLY=%s WHERE MONTH=%s""",
                       (total, daily, monthly, month))
    except mysql.connector.Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        conexion.close()
        return  # Exit the function on error

    conexion.commit()
    cursor.close()
    conexion.close()
    print("Registro editado correctamente!")


def cerrarConex():
    cursor.close()
    conexion.close()


def verTodoProd():
    try:
        cursor.execute("SELECT * FROM productos")
    except mysql.connector.Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        conexion.close()
        return  # Exit the function on error
    # Obtener los resultados
    fila = cursor.fetchall()
    return fila

def editarRate(id, rate):
    # Editar el registro
    try:
        cursor.execute(f"""UPDATE productos SET rate=%s WHERE ID=%s""",
                       (rate, id))
    except mysql.connector.Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        conexion.close()
        return  # Exit the function on error
    conexion.commit()
    print('Ratio modificado')


def resetRate():
    try:
        cursor.execute("UPDATE productos SET rate = 0")
    except mysql.connector.Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        return  # Exit the function on error
    conexion.commit()


def orderByRateDESC():
    try:
        # Conectar a la base de datos
        conexion = mysql.connector.connect(**config)
        print('Conexión exitosa')

        # Crear un cursor
        cursor = conexion.cursor()

        # Ejecutar la consulta con ORDER BY
        cursor.execute("SELECT * FROM productos ORDER BY rate DESC LIMIT 3")

        # Obtener los resultados
        filas = cursor.fetchall()

        # Imprimir los resultados
        return filas

    except mysql.connector.Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        return None


def orderByRateASC():
    try:
        # Conectar a la base de datos
        conexion = mysql.connector.connect(**config)
        print('Conexión exitosa')

        # Crear un cursor
        cursor = conexion.cursor()

        # Ejecutar la consulta con ORDER BY
        cursor.execute("SELECT * FROM productos ORDER BY rate ASC LIMIT 3")

        # Obtener los resultados
        filas = cursor.fetchall()

        # Imprimir los resultados
        return filas

    except mysql.connector.Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        return None


def editinflat(monthly, month):
    try:
        conexion = mysql.connector.connect(**config)
        print('Conexion exitosa')
    except mysql.connector.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return  # Exit the function on error

    cursor = conexion.cursor()

    try:
        cursor.execute("""UPDATE inflation SET MONTHLY=%s, MONTH=%s""",
                       (monthly, month))
    except mysql.connector.Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        conexion.close()
        return  # Exit the function on error

    conexion.commit()
    print("Inicio de mes!")
