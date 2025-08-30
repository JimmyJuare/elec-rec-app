from datetime import datetime
from .db import db

class Lead(db.Model):
    __tablename__ = "leads"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    contact = db.Column(db.String(255))     # email/phone
    source = db.Column(db.String(255))      # LinkedIn, GitHub, Indeed
    status = db.Column(db.String(64))       # e.g., "new","contacted","interested"
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
