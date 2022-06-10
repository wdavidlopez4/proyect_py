import uuid
from src.DAL.db import db


class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.VARCHAR(36), primary_key=True)
    name = db.Column(db.VARCHAR(10))
    password = db.Column(db.VARCHAR(100))
    mail = db.Column(db.VARCHAR(30))
    isLogin = db.Column(db.Boolean)
    publications = db.relationship('Publications')

    def __init__(self, name, mail, password):
        self.id = str(uuid.uuid4())
        self.name = name
        self.mail = mail
        self.password = password

    def loguin(self, name, password):
        if(self.name == name) and (self.password == password):
            self.isLogin = True

    def logout(self):
        self.isLogin = False

    def change(self, name, password):
        self.name = name
        self.password = password

