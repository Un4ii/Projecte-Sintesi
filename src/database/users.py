import mysql.connector
import os

db_info = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWD"),
    "database": os.getenv("DB_DATABASE"),
}

def createNewUser(user_id, name, surname, passwd, mail, vegetarian, vegan, age, weight, height, sex, allergies, intolerances):
    conn = mysql.connector.connect(**db_info)
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO Usuarios (ID, Nombre, Apellido, Contrasena, Correo, Vegetariano, Vegano, Edad, Peso, Altura, Sexo, Alergias, Intolerancias)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (user_id, name, surname, passwd, mail, vegetarian, vegan, age, weight, height, sex, allergies, intolerances))
        conn.commit()
        
        cursor.execute("SELECT * FROM Usuarios WHERE ID = %s", (user_id,))
        response = cursor.fetchone()

        if response:
            return True, "Usuario creado exitosamente"
        else:
            return False, "Error al crear usuario"

    except mysql.connector.Error as err:
        conn.rollback()
        return False, f"Error en la base de datos: {err}"

    finally:
        cursor.close()
        conn.close()


def getUserData(user_id):
    conn = mysql.connector.connect(**db_info)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM Usuarios WHERE ID = %s", (user_id,))
        data = cursor.fetchall()

        if data:
            data = data[0]
            result = {
                "id": data[0],
                "nombre": data[1],
                "apellido": data[2],
                "correo": data[4],
                "vegetariano": data[5],
                "vegano": data[6],
                "edad": data[7],
                "peso": data[8],
                "altura": data[9],
                "sexo": data[10],
                "alergias": data[11],
                "intolerancias": data[12],
            }
            return True, result
        else:
            return False, "Usuario no encontrado"
    
    except mysql.connector.Error as err:
        return False, f"Error en la base de datos: {err}"

    finally:
        cursor.close()
        conn.close()


def deleteUser(user_id):
    conn = mysql.connector.connect(**db_info)
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM Usuarios WHERE ID = %s", (user_id,))
        conn.commit()

        if cursor.rowcount > 0:
            return True, "Usuario eliminado exitosamente"
        else:
            return False, "Usuario no encontrado"

    except mysql.connector.Error as err:
        conn.rollback()
        return False, f"Error en la base de datos: {err}"

    finally:
        cursor.close()
        conn.close()


def changePasswd(user_id, new_passwd):
    conn = mysql.connector.connect(**db_info)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT Contrasena FROM Usuarios WHERE ID = %s", (user_id,))
        data = cursor.fetchone() 

        if data:
            current_password = data[0]
            
            if current_password != new_passwd:
                cursor.execute("UPDATE Usuarios SET Contrasena = %s WHERE ID = %s", (new_passwd, user_id))
                conn.commit()
                return True, "Contraseña actualizada correctamente"
            else:
                return False, "La nueva contraseña no puede ser la misma que la actual"
        else:
            return False, "Usuario no encontrado"

    except mysql.connector.Error as err:
        conn.rollback()
        return False, f"Error en la base de datos: {err}"

    finally:
        cursor.close()
        conn.close()
