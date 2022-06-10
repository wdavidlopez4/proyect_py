from src.BLL.entities.User import User
from src.DAL.db import db


class UsersServices:

    def add(self, objJSON):
        user = User(
            objJSON['name'],
            objJSON['mail'],
            objJSON['password']
        )

        db.session.add(user)
        db.session.commit()
        return 0

    def update(self, objJSON):
        user = User.query.get(objJSON['id'])
        user.change(objJSON['name'],
                           objJSON['password'])

        db.session.commit()
        return 0

    def delete(self, objJSON):
        user = User.query.get(objJSON['id'])
        db.session.delete(user)
        db.session.commit()

    def get(self, id):
        user = User.query.get(id)
        return user.to_json()

    def login(self, id):
        user = User.query.get(id)
        user.loguin(user.name, user.password)

    def logout(self, id):
        user = User.query.get(id)
        user.logout()
