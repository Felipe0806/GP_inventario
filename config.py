import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'mi_clave_secreta'  # Cambia esto por algo más seguro en producción
    SQLALCHEMY_DATABASE_URI = (
        'postgresql://postgres:Baseuser0806@userdb.ckkft1kjllti.us-east-1.rds.amazonaws.com:5432/UserManagement'
    )
