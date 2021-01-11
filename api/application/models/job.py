from application.database import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(100))
    title = db.Column(db.String(100))
    company = db.Column(db.String(255))
    location = db.Column(db.String(100))
    description = db.Column(db.String)
    requirements = db.Column(db.String)
    qualifications = db.Column(db.String)
    salary = db.Column(db.String)
    application = db.Column(db.String)
