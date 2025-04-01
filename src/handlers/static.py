from src.utils import Response
from flask import send_from_directory, request
import os

from src.utils import decodeToken

def serveStaticUser(filename):
    allowed_extensions = {"png", "jpg", "webp", "jpeg", "webm"}
    directory = os.path.join(os.getenv("STATIC_PATH"), "user")
    
    for ext in allowed_extensions:
        file = os.path.join(directory, f"{filename}.{ext}")
        if os.path.isfile(file):
            return send_from_directory(directory, f"{filename}.{ext}")
    
    return Response({
        "error": "Not Found",
        "message": "El recurso que buscas no fue encontrado."
    }, 404)
        
    
def serveStaticContent(filename):
    allowed_extensions = {"png", "jpg", "webp", "jpeg", "webm"}
    directory = os.path.join(os.getenv("STATIC_PATH"), "content")
    
    for ext in allowed_extensions:
        file = os.path.join(directory, f"{filename}.{ext}")
        if os.path.isfile(file):
            return send_from_directory(directory, f"{filename}.{ext}")
    
    return Response({
        "error": "Not Found",
        "message": "El recurso que buscas no fue encontrado."
    }, 404)
    
def uploadStaticUser():
    
    token_ok, token_response = decodeToken(request.headers.get("Authorization"), request.headers.get("user"))
    
    if not token_ok:
        return Response({
            "error": "Bad authorization",
            "message": token_response
        }, 401)
    
    if "file" not in request.files:
        return Response({
            "error": "Bad Request",
            "message": "No file part in request."
        }, 400)

    file = request.files["file"]

    if file.filename == "":
        return Response({
            "error": "Bad Request",
            "message": "No selected file."
        }, 400)

    ext = file.filename.rsplit(".", 1)[1].lower() if "." in file.filename else ""
    if ext not in {"png", "jpg", "webp", "jpeg", "webm"}:
        return Response({
            "error": "Bad Request",
            "message": "Invalid file type."
        }, 400)

    directory = os.path.join(os.getenv("STATIC_PATH"), "user")

    file_path = os.path.join(directory, f"{token_response}.{ext}")
    os.makedirs(directory, exist_ok=True)
    file.save(file_path)

    return Response({
        "message": "File uploaded successfully.",
        "filename": file.filename
    }, 201)