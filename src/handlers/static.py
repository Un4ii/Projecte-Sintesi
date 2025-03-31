from src.utils import Response
from flask import send_from_directory, request
import os

def serveStaticUser(filename):
        if not ("." in filename and filename.rsplit(".", 1)[1].lower() in {"png", "jpg", "webp", "jpeg", "webm"}):
            return Response({
                "error": "Not Found",
                "message": "El recurso que buscas no fue encontrado."
            }, 404)
            
        directory = os.path.join(os.getenv("STATIC_PATH"), "user")
        file = os.path.join(directory, filename)
        
        if not os.path.isfile(file):
            return Response({
                "error": "Not Found",
                "message": "El recurso que buscas no fue encontrado."
            }, 404)
        
        return send_from_directory(directory, filename)
    
def serveStaticContent(filename):
        if not ("." in filename and filename.rsplit(".", 1)[1].lower() in {"png", "jpg", "webp", "jpeg", "webm"}):
            return Response({
                "error": "Not Found",
                "message": "El recurso que buscas no fue encontrado."
            }, 404)
            
        directory = os.path.join(os.getenv("STATIC_PATH"), "content")
        file = os.path.join(directory, filename)
        
        if not os.path.isfile(file):
            return Response({
                "error": "Not Found",
                "message": "El recurso que buscas no fue encontrado."
            }, 404)
        
        return send_from_directory(directory, filename)
    
def uploadStaticUser():
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

    file_path = os.path.join(directory, file.filename)
    os.makedirs(directory, exist_ok=True)
    file.save(file_path)

    return Response({
        "message": "File uploaded successfully.",
        "filename": file.filename
    }, 201)