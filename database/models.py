from typing import List

from extensions import db


class Collections(db.Document):
    name = db.StringField(max_length=20, unique=True)


class Pricing(db.EmbeddedDocument):
    price = db.FloatField()
    compare_at_price = db.FloatField()
    cost_per_item = db.FloatField()


class Inventory(db.EmbeddedDocument):
    sku = db.StringField()
    barcode = db.StringField()
    quantity = db.IntField()
    track_quantity = db.BooleanField(default=True)


class Options(db.EmbeddedDocument):
    size = db.ListField(db.StringField(max_length=30))
    color = db.ListField(db.StringField(max_length=30))
    material = db.ListField(db.StringField(max_length=30))
    style = db.ListField(db.StringField(max_length=30))


class Products(db.Document):
    title = db.StringField(required=True)
    description = db.StringField()
    pricing = db.EmbeddedDocumentField(Pricing)

    inventory = db.EmbeddedDocumentField(Inventory)

    product_type = db.StringField()
    vendor = db.StringField()
    tags = db.ListField(db.StringField(max_length=30))
    variants = db.EmbeddedDocumentField(Options)

    collection = db.ReferenceField(Collections)
