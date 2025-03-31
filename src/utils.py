from flask import make_response, jsonify
import jwt
import datetime

JWT_TOKEN = "1yjbcYUoo5xrzHlZERCLXKtqTqm4D5KaWU2ES4O2dHv5E8RCAL6AqkSFuHKgJyuJ"

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

    token = jwt.encode(payload, JWT_TOKEN, algorithm='HS256')
    
    return token

def decodeToken(token):
    try:
        payload = jwt.decode(token, JWT_TOKEN, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
