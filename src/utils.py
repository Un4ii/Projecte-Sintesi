from flask import make_response, jsonify
import jwt
import datetime
import os

def Response(data=None, statusCode=200, headers={"Content-Type": "application/json"}):
    if data is None:
        data = {}
    
    response = make_response(jsonify(data), statusCode)
    response.headers.update(headers)
    return response

def genToken(user_id):
    expiration_time = datetime.timedelta(hours=1)

    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + expiration_time
    }

    token = jwt.encode(payload, os.getenv("JWT_TOKEN"), algorithm='HS256')
    
    return token

def decodeToken(token, user_id):
    try:    
        if not token:
            return False, "Token no proporcionado"
        
        token = token.split(" ")[1]
        user_data = jwt.decode(token, os.getenv("JWT_TOKEN"), algorithms=['HS256'])

        if user_data is None:
            return False, "Token invalido o expirado"
        
        if user_id != user_data['user_id']:
            return False, "user_id invalido"
        
        
        if user_data['user_id'] == user_id:
            return True, user_data['user_id']

        else:
            return False, "El token no pertenece al usuario proporcionado"
            
    except jwt.ExpiredSignatureError:
        return False, "Token invalido o expirado"
    
    except jwt.InvalidTokenError:
        return False, "Token invalido o expirado"
