import uuid
from src.DAL.db import db
from datetime import datetime
from src.BLL.entities.Priority import Priority
from src.BLL.entities.Status import Status


class Publication(db.Model):
    __tablename__ = 'Publications'

    id = db.Column(db.VARCHAR(36), primary_key=True)
    title = db.Column(db.VARCHAR(10))
    description = db.Column(db.VARCHAR(100))
    priority = db.Column(db.Integer)
    status = db.Column(db.Integer)
    time = db.Column(db.DateTime)
    user_id = db.Column(db.VARCHAR(36),
                        db.ForeignKey('Users.id'),
                        nullable=True)

    def __init__(self, title, description, priority: Priority, user_id):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.priority = priority
        self.status = Status.sin_publicar.value
        self.time = datetime.now()
        self.user_id = user_id

    def post(self):
        self.status.publicada

    def change(self, title, description, priority: Priority):
        self.title = title
        self.description = description
        self.priority = priority

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'status': self.status,
            'time': self.time
        }