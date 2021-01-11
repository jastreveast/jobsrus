from application.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(50))
    admin = db.Column(db.Boolean, default=False)
    