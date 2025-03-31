from flask import Flask, request
from src.utils import Response, genToken, decodeToken

app = Flask(__name__)

@app.route("/status", methods=["GET"])
def status():
    return Response({
        "status": "ok",
    })

@app.route("/token", methods=["GET"])
def token():
    user_id = request.args.get("user_id")

    if not user_id: 
        return Response({"error":"user_id invalido"})
    
    return Response({
        "token": genToken(user_id),
    })
    
@app.route("/check", methods=["GET"])
def check():
    
    token = request.headers.get('Authorization')
    
    if not token:
        return Response({"error": "Token no proporcionado"}, statusCode=401)
    
    token = token.split(" ")[1]
    user_data = decodeToken(token)
    user_id = request.args.get("user_id")

    if user_data is None:
        return Response({"error": "Token inválido o expirado"}, statusCode=401)
    
    if user_id != user_data['user_id']:
        return Response({"error":"user_id invalido"})
    
    return Response({"message": "Acceso autorizado", "user_id": user_data['user_id']})
    
# Errores
@app.errorhandler(404)
def page_not_found(error):
    return Response({
        "error": "Not Found",
        "message": "The resource you are looking for was not found."
    }, 404)

@app.errorhandler(500)
def internal_error(error):
    return Response({
        "error": "Internal Server Error",
        "message": "An unexpected error occurred on the server."
    }, 500)

@app.errorhandler(Exception)
def handle_exception(error):
    return Response({
        "error": "Server Error",
        "message": "Something went wrong, please try again later."
    }, 500)


if __name__ == "__main__":
    app.run(debug=True)
