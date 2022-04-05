from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class EmailListaNegra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    motivo = db.Column(db.String(255))
    ip = db.Column(db.String(100))
    id_app = db.Column(db.String(100))
    fecha_solicitud = db.Column(db.DateTime(timezone=False))

class ListaNegrachema(SQLAlchemyAutoSchema):
    class Meta:
        model = EmailListaNegra
        include_relationships = True
        load_instance = True
