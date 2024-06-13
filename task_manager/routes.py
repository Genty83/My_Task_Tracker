# IMPORTS
from flask import render_template, request, redirect, url_for
from task_manager import app, db
from task_manager.models import Category, Task


# HOMEPAGE
@app.route("/")
def home():
    return render_template("tasks.html")


# CATEGORIES
@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())

    return render_template("categories.html", categories=categories)


# HOMEPAGE
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")


# HOMEPAGE
@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)


# HOMEPAGE
@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))