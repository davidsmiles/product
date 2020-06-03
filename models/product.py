from typing import List

from extensions import db


class Pricing(db.EmbeddedDocument):
    price = db.FloatField()
    compare_at_price = db.FloatField()
    cost_per_item = db.FloatField()


class Inventory(db.EmbeddedDocument):
    sku = db.StringField()
    barcode = db.StringField()
    quantity = db.IntField()
    track_quantity = db.BooleanField(default=True)


class Products(db.Document):
    title = db.StringField(required=True)
    description = db.StringField()
    pricing = db.EmbeddedDocumentField(Pricing)

    inventory = db.EmbeddedDocumentField(Inventory)

    product_type = db.StringField()
    vendor = db.StringField()
    tags = db.ListField(db.StringField(max_length=30))
