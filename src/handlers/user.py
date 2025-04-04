from flask import request

from src.utils import Response, decodeToken
from src.database.users import DBgetUserData, DBcreateNewUser, DBdeleteUser, DBchangePasswd

def getUserProfile(user_id):
    token_ok, token_response = decodeToken(request.headers.get("Authorization"), request.headers.get("user"))
    
    if not token_ok:
        return Response({
            "error": "Error al obtener el usuario",
            "message": token_response
        }, 401)
              
    status, code, response = DBgetUserData(user_id)
    
    if not status:
        return Response({
            "error": "Error al obtener el usuario",
            "message": response
        }, code)
        
    return Response(response)