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

def decodeToken(token):
    try:
        payload = jwt.decode(token, os.getenv("JWT_TOKEN"), algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
