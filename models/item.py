from typing import List

from extensions import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(40), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)

    # store_id = db.Column(db.Integer, nullable=False)

    @classmethod
    def find_by_id(cls, item_id) -> 'ItemModel':
        return cls.query.filter_by(id=item_id).first()

    @classmethod
    def find_by_name(cls, name) -> 'ItemModel':
        return cls.query.filter_by(name=name).first()

    # @classmethod
    # def find_by_store_id(cls, store_id) -> 'ItemModel':
    #     return cls.query.filter_by(store_id=store_id)

    @classmethod
    def find_all(cls) -> List['ItemModel']:
        return cls.query.all()

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        self.save_to_db()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
