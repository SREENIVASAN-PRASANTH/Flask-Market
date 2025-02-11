from market import db

class Item(db.Model):
    id = db.Column(db.Integer(),primary_key = True)
    name = db.Column(db.String(30), nullable = False, unique = True)
    barcode = db.Column(db.String(10), nullable = False, unique = True)
    price = db.Column(db.Integer(), nullable = False)
    description = db.Column(db.String(30), nullable = False, unique = True)

    def __repr__(self):
        return f"Item {self.name}"