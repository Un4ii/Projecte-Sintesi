import mysql.connector
import os

db_info = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWD"),
    "database": os.getenv("DB_DATABASE"),
}

def getAllergies():
    conn = mysql.connector.connect(**db_info)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM Alergias")
        data = cursor.fetchall()
                
        if data:
            response = []
            for item in data:
                response.append({
                    "id": item[0],
                    "nombre": item[1],
                })    
            
            return True, response
        
        else:
            return False, f"No se ha encontrado ningun elemento."
        
    except mysql.connector.Error as err:
        conn.rollback()
        return False, f"Error en la base de datos: {err}"

    finally:
        cursor.close()
        conn.close()
        
def getIntolerances():
    conn = mysql.connector.connect(**db_info)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM Intolerancias")
        data = cursor.fetchall()
        
        if data:
            response = []
            for item in data:
                response.append({
                    "id": item[0],
                    "nombre": item[1],
                })    
            
            return True, response

        else:
            return False, f"No se ha encontrado ningun elemento."
        
    except mysql.connector.Error as err:
        conn.rollback()
        return False, f"Error en la base de datos: {err}"

    finally:
        cursor.close()
        conn.close()
        
def getAllergy(allergy_id):
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

            return True, response

        else:
            return False, f"No se ha encontrado ningun elemento."
        
    except mysql.connector.Error as err:
        conn.rollback()
        return False, f"Error en la base de datos: {err}"

    finally:
        cursor.close()
        conn.close()
        
def getIntolerance(intolerance_id):
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

            return True, response

        else:
            return False, f"No se ha encontrado ningun elemento."
        
    except mysql.connector.Error as err:
        conn.rollback()
        return False, f"Error en la base de datos: {err}"

    finally:
        cursor.close()
        conn.close()