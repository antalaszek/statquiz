from app import db
import json


class Distribution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    svg = db.Column(db.Text, nullable=False)
    formula = db.Column(db.Text, nullable=False)
    parameters = db.Column(db.Text)  # Changed to Text to store JSON string

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "svg": self.svg,
            "formula": self.formula,
            "parameters": json.loads(self.parameters) if self.parameters else None,
        }
