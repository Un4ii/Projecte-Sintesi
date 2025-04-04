from flask import request

from src.utils import Response, decodeToken
from src.database.others import DBgetAllergies, DBgetAllergy, DBgetIntolerance, DBgetIntolerances, DBgetAllergiesByIds, DBgetIntolerancesByIds

def getAllergies():
    token_ok, token_response = decodeToken(request.headers.get("Authorization"), request.headers.get("user"))
    
    if not token_ok:
        return Response({
            "error": "Error al obtener la alergia.",
            "message": token_response
        }, 401)
    
    allergies = request.args.get("id")
    if not allergies:
        return Response({
            "error": "Error al obtener la alergia.",
            "message": "No se ha proporcionado ID"
        }, 400)
        
    else:
        allergies = allergies.split(",")
        print( len(allergies) )
        if len(allergies) > 1:
            status, code, response = DBgetAllergiesByIds(allergies)
        else:
            status, code, response = DBgetAllergy(allergies[0])
            
    
    if not status:
        return Response({
            "error": "Error al obtener la alergia.",
            "message": response
        }, code)
        
    return Response(response)

def getIntolerances():
    token_ok, token_response = decodeToken(request.headers.get("Authorization"), request.headers.get("user"))
    
    if not token_ok:
        return Response({
            "error": "Error al obtener la alergia.",
            "message": token_response
        }, 401)
    
    intolerances = request.args.get("id")
    if not intolerances:
        return Response({
            "error": "Error al obtener la alergia.",
            "message": "No se ha proporcionado ID"
        }, 400)
        
    else:
        intolerances = intolerances.split(",")
        print( len(intolerances) )
        if len(intolerances) > 1:
            status, code, response = DBgetIntolerancesByIds(intolerances)
        else:
            status, code, response = DBgetIntolerance(intolerances[0])
            
    
    if not status:
        return Response({
            "error": "Error al obtener la alergia.",
            "message": response
        }, code)
        
    return Response(response)

def getAllAllergies():
    token_ok, token_response = decodeToken(request.headers.get("Authorization"), request.headers.get("user"))
    
    if not token_ok:
        return Response({
            "error": "Error al obtener las alergias.",
            "message": token_response
        }, 401)

    status, code, response = DBgetAllergies()
    
    if not status:
        return Response({
            "error": "Error al obtener las alergias.",
            "message": response
        }, code)
        
    return Response(response)


def getAllIntolerances():
    token_ok, token_response = decodeToken(request.headers.get("Authorization"), request.headers.get("user"))
    
    if not token_ok:
        return Response({
            "error": "Error al obtener las intolerancias.",
            "message": token_response
        }, 401)

    status, code, response = DBgetIntolerances()
    
    if not status:
        return Response({
            "error": "Error al obtener las intolerancias.",
            "message": response
        }, code)
        
    return Response(response)
