from flask import Flask, request
from dotenv import load_dotenv

from src.utils import Response, genToken
from src.handlers.static import serveStaticContent, serveStaticUser, uploadStaticUser
from src.handlers.other import getAllergies, getAllAllergies, getIntolerances, getAllIntolerances
from src.handlers.user import getUserProfile 

load_dotenv()

app = Flask(__name__)

# ---- Health CHeck ----
@app.route("/status", methods=["GET"])
def get_status():
    return Response({
        "status": "ok",
    })
    
# ---- Static ----
@app.route("/static/content/<user_id>", methods=["GET"])
def get_static_content(user_id):
    return serveStaticContent(user_id)

@app.route("/static/user/<user_id>", methods=["GET"])
def get_static_user(user_id):
    return serveStaticUser(user_id)

@app.route("/static/upload", methods=["POST"])
def post_static_upload():
    return uploadStaticUser()


# ---- Others ----
@app.route("/allergies", methods=["GET"])
def get_other_allergies():
    if request.args.get("id"):
        return getAllergies()
    else:
        return getAllAllergies()
    
@app.route("/intolerances", methods=["GET"])
def get_other_intolerances():
    if request.args.get("id"):
        return getIntolerances()
    else:
        return getAllIntolerances()


# ---- User ----
@app.route("/user/profile/<user_id>", methods=["GET"])
def get_user_profile(user_id):
    return getUserProfile(user_id)






@app.route("/token", methods=["GET"])
def token():
    user_id = request.args.get("user")

    if not user_id: 
        return Response({"error":"user_id invalido"})
    
    return Response({
        "token": genToken(user_id),
    })
    
# Errores
@app.errorhandler(404)
def page_not_found(error):
    return Response({
        "error": "Not Found",
        "message": "El recurso que buscas no fue encontrado."
    }, 404)

@app.errorhandler(500)
def internal_error(error):
    return Response({
        "error": "Internal Server Error",
        "message": "Ocurrio un error inesperado en el servidor."
    }, 500)

@app.errorhandler(Exception)
def handle_exception(error):
    return Response({
        "error": "Server Error",
        "message": "Algo salio mal, por favor intenta nuevamente mas tarde."
    }, 500)


if __name__ == "__main__":
    app.run(debug=True)
