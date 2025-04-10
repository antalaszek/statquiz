from flask import jsonify
from app import app, db
from app.models import Distribution
from sqlalchemy import select


@app.route("/api/questions", methods=["GET"])
def get_questions():
    # Create a select statement for the Distribution model.
    stmt = select(Distribution)
    # Execute the statement; scalars() extracts the actual Distribution instances.
    distributions = db.session.scalars(stmt).all()
    # Serialize the objects using their own to_dict() method.
    return jsonify([d.to_dict() for d in distributions])
