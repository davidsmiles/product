from typing import List

from extensions import db


class Collections(db.Document):
    title = db.StringField(required=True, unique=True, max_length=20)


class Pricing(db.EmbeddedDocument):
    price = db.FloatField()
    compare_at_price = db.FloatField()
    cost_per_item = db.FloatField()


class Inventory(db.EmbeddedDocument):
    sku = db.StringField()
    barcode = db.StringField()
    quantity = db.IntField()
    track_quantity = db.BooleanField()


class Options(db.EmbeddedDocument):
    size = db.ListField(db.StringField(max_length=30))
    color = db.ListField(db.StringField(max_length=30))
    material = db.ListField(db.StringField(max_length=30))
    style = db.ListField(db.StringField(max_length=30))


class Products(db.Document):
    title = db.StringField(required=True)
    description = db.StringField(default="")

    pricing = db.EmbeddedDocumentField(Pricing, default=Pricing(price=0.00, compare_at_price=0.00, cost_per_item=0.00))

    inventory = db.EmbeddedDocumentField(Inventory, default=Inventory(sku="", barcode="", quantity=0, track_quantity=True))

    type = db.StringField()
    vendor = db.StringField()
    tags = db.ListField(db.StringField(max_length=30))
    variants = db.EmbeddedDocumentField(Options)

    collections = db.ListField(db.ReferenceField(Collections))
