from .. import db

class Student(db.Model):
    """
    Database model for our Student class
    """
    # Allows us to specify the name of our table. If we don't add this line,
    # SQLAlchemy automatically generates the table name from our class name.
    __tablename__ = "students"

    # Primary keys differentiate between unique entries in the database
    # This is automatically generated for us. Thanks SQLAlchemy!
    id = db.Column(db.Integer, primary_key=True)
    # Columns are properties/attributes
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    year = db.Column(db.Integer)
