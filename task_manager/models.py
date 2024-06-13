# IMPORTS
from task_manager import db


class Catagory(db.Model):
    # Schema for the catagory model
    id = db.Column(db.Integer, primary_key=True)
    catagory_name = db.Column(db.String(25), unique=True, nullable= False)
    tasks = db.relationship("Task", backref="catagory", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent a string of the object
        return self.catagory_name


class Task(db.Model):
    # Schema for the task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable= False)
    task_description = db.Column(db.Text(), nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    catagory_id = db.Column(db.Integer, db.ForeignKey("catagory.id", ondelete="CASCADE"), nullable=False)


    def __repr__(self):
        # __repr__ to represent a string of the object
        return f"{self.task_name}{self.task_description}{self.is_urgent}{self.id}"