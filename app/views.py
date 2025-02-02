from flask import redirect, render_template
from app import app

from . import db
from .models import Student
from .forms import AddStudentForm


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


# We can allow the user/client to give us data through the route.
@app.route("/<name>/<int:rating>", methods=['GET'])
def welcome(name, rating):
    return render_template('welcome.html', name=name, rating=rating)


@app.route("/students", methods=['GET'])
def view_students():
    """View all students."""
    # Get all the students from the database
    students = Student.query.all()
    # Pass it to the frontend
    return render_template('students.html', students=students)


# Note that in methods we also added 'POST'. This allows the client to send info
# back to the server.
@app.route("/students/add", methods=['GET', 'POST'])
def add_students():
    """Add a new student."""
    # First we create a new form
    form = AddStudentForm()
    # If the form is validated:
    if form.validate_on_submit():
        # Create a new student based on the data in the form
        student = Student(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            year=form.year.data
        )
        # Add and commit the data to the database
        db.session.add(student)
        # Data must be committed or it won't actually show up
        db.session.commit()
        return redirect('/students')
    # Here we specify which template to be rendered and the form we want to use
    return render_template('add_students.html', form=form)
