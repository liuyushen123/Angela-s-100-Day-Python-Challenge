from flask import Blueprint, render_template, request, redirect, url_for

pages_bp = Blueprint("pages", __name__)


@pages_bp.route("/contact")
def contact_page():
    return render_template("contact.html")


@pages_bp.route("/login", methods=["POST", "GET"])
def receive_data():
    username = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    return "<h1>Thank you for your submission!</h1><p>Name: {}</p><p>Email: {}</p><p>Message: {}</p>".format(
        username, email, message
    )
