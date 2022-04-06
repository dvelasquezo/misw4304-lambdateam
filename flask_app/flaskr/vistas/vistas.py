from datetime import datetime

from flask_restful import Resource
from ..modelos import db, EmailListaNegra
from flask import request
import uuid

class VistaBlacklistsPost(Resource):
    def post(self):
        if (EmailListaNegra.query.filter(EmailListaNegra.email == request.json["email"]).first()) != None:
            return "El email ya existe en la lista negra", 403
        nuevo_email = EmailListaNegra(email=request.json["email"], motivo=request.json["motivo"], ip=request.remote_addr, id_app=str(uuid.uuid1()), fecha_solicitud=datetime.now())
        db.session.add(nuevo_email)
        db.session.commit()
        return 'El email fue agregagado correctamente a la lista negra', 200

class VistaBlacklistsGet(Resource):
    def get(self, email):
       email_consultado = EmailListaNegra.query.filter(EmailListaNegra.email == email).first()
       if email_consultado != None:
           return {"email": email_consultado.email, "Motivo": email_consultado.motivo}

       return "El email no esta en la lista negra", 200

class VistaRoot(Resource):
    def get(self):
        return 'Ok', 200

    def post(self):
        return 'Ok', 200
