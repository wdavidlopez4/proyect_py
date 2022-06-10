from src.BLL.entities.Publication import Publication
from src.DAL.db import db


class PublicationsServices:

    def add(self, objJSON):
        publication = Publication(
            objJSON['title'],
            objJSON['description'],
            objJSON['priority'],
            objJSON['user_id']
        )

        db.session.add(publication)
        db.session.commit()
        return 0

    def postMessage(self, objJSON):
        pub = Publication.query.get(objJSON['id'])
        pub.post()
        return 0

    def update(self, objJSON):
        publication = Publication.query.get(objJSON['id'])
        publication.change(objJSON['title'],
                           objJSON['description'],
                           objJSON['priority'])

        db.session.commit()
        return 0

    def delete(self, objJSON):
        publication = Publication.query.get(objJSON['id'])
        db.session.delete(publication)
        db.session.commit()

    def get(self, id):
        publication = Publication.query.get(id)
        return publication.to_json()