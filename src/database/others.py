import mysql.connector
import os

db_info = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWD"),
    "database": os.getenv("DB_DATABASE"),
}

def DBgetAllergies():
    conn = mysql.connector.connect(**db_info)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM Alergias")
        data = cursor.fetchall()

        if data:
            response = [{"id": item[0], "nombre": item[1]} for item in data]
            return True, 200, response
        else:
            return False, 404, "No se ha encontrado ningún elemento"

    except mysql.connector.Error:
        conn.rollback()
        return False, 500, "Error en la base de datos"

    finally:
        cursor.close()
        conn.close()


def DBgetIntolerances():
    conn = mysql.connector.connect(**db_info)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM Intolerancias")
        data = cursor.fetchall()

        if data:
            response = [{"id": item[0], "nombre": item[1]} for item in data]
            return True, 200, response
        else:
            return False, 404, "No se ha encontrado ningún elemento"

    except mysql.connector.Error:
        conn.rollback()
        return False, 500, "Error en la base de datos"

    finally:
        cursor.close()
        conn.close()


def DBgetAllergy(allergy_id):
    conn = mysql.connector.connect(**db_info)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM Alergias WHERE ID = %s", (allergy_id,))
        data = cursor.fetchall()

        if data:
            data = data[0]
            response = {
                "id": data[0],
                "nombre": data[1],
            }
            return True, 200, response
        else:
            return False, 404, "No se ha encontrado ningún elemento"

    except mysql.connector.Error:
        conn.rollback()
        return False, 500, "Error en la base de datos"

    finally:
        cursor.close()
        conn.close()


def DBgetIntolerance(intolerance_id):
    conn = mysql.connector.connect(**db_info)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM Intolerancias WHERE ID = %s", (intolerance_id,))
        data = cursor.fetchall()

        if data:
            data = data[0]
            response = {
                "id": data[0],
                "nombre": data[1],
            }
            return True, 200, response
        else:
            return False, 404, "No se ha encontrado ningún elemento"

    except mysql.connector.Error:
        conn.rollback()
        return False, 500, "Error en la base de datos"

    finally:
        cursor.close()
        conn.close()

def DBgetAllergiesByIds(ids):
    if not ids:
        return False, 400, "La lista de IDs está vacía"

    conn = mysql.connector.connect(**db_info)
    cursor = conn.cursor()

    try:
        format_strings = ','.join(['%s'] * len(ids))
        query = f"SELECT * FROM Alergias WHERE ID IN ({format_strings})"
        cursor.execute(query, tuple(ids))
        data = cursor.fetchall()

        if data:
            response = [{"id": item[0], "nombre": item[1]} for item in data]
            return True, 200, response
        else:
            return False, 404, "No se ha encontrado ningún elemento"

    except mysql.connector.Error:
        conn.rollback()
        return False, 500, "Error en la base de datos"

    finally:
        cursor.close()
        conn.close()


def DBgetIntolerancesByIds(ids):
    if not ids:
        return False, 400, "La lista de IDs está vacía"

    conn = mysql.connector.connect(**db_info)
    cursor = conn.cursor()

    try:
        format_strings = ','.join(['%s'] * len(ids))
        query = f"SELECT * FROM Intolerancias WHERE ID IN ({format_strings})"
        cursor.execute(query, tuple(ids))
        data = cursor.fetchall()

        if data:
            response = [{"id": item[0], "nombre": item[1]} for item in data]
            return True, 200, response
        else:
            return False, 404, "No se ha encontrado ningún elemento"

    except mysql.connector.Error:
        conn.rollback()
        return False, 500, "Error en la base de datos"

    finally:
        cursor.close()
        conn.close()
