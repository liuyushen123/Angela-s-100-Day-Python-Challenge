from flask import Flask, jsonify, render_template, request, Blueprint, redirect, url_for
from model import Cafe
import random

routes_bp = Blueprint("routes", __name__)
# HTTP GET - Read Record


@routes_bp.route("/")
def home():
    return render_template("index.html")


@routes_bp.route("/random")
def get_random():
    random_cafe = Cafe.get_random_cafe()
    if random_cafe:
        return jsonify(random_cafe.to_dict())

    return {"error": "No coffee shops found."}


@routes_bp.route("/all")
def get_all():
    all_cafe = Cafe.get_all_cafes()

    print([cafe.to_dict() for cafe in all_cafe])

    return jsonify([cafe.to_dict() for cafe in all_cafe])


@routes_bp.route("/search")
def search_cafe():
    attribute = request.args.get("attribute")
    value = request.args.get("value")
    if not attribute or not value:
        return jsonify(error="Both 'attribute' and 'value' are required"), 400

    try:
        cafes = Cafe.find_cafe(attribute, value)
    except ValueError as e:
        return jsonify(error=str(e)), 400

    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@routes_bp.route("/first")
def get_first():
    first_cafe = Cafe.get_first_cafe()
    if first_cafe:
        return jsonify(first_cafe.to_dict())

    return {"error": "No coffee shops found."}


@routes_bp.route("/last")
def get_last():
    last_cafe = Cafe.get_last_cafe()
    if last_cafe:
        return jsonify(last_cafe.to_dict())
    return {"error": "No coffee shops found."}


# HTTP POST - Create Record
@routes_bp.route("/add", methods=["GET", "POST"])  # type: ignore
def add_cafe():
    Cafe().add_cafe(
        request.args.get("name"),
        request.args.get("map_url"),
        request.args.get("img_url"),
        request.args.get("loc"),
        request.args.get("seats"),
        bool(request.args.get("toilet")),
        bool(request.args.get("wifi")),
        bool(request.args.get("sockets")),
        bool(request.args.get("calls")),
        request.args.get("coffee_price"),
    )

    return jsonify({"Success": "Cafe added"})


# HTTP PUT/PATCH - Update Record
@routes_bp.route("/update-attribute", methods=["PATCH"])
def update_attribute():
    message = Cafe.update_cafe(
        cafe_id=request.args.get("id"),
        attribute=request.args.get("attribute"),
        value=request.args.get("value"),
    )

    return jsonify({"Message": message})


# HTTP DELETE - Delete Record
@routes_bp.route("/delete-cafe")
def delete():

    message = Cafe.delete_cafe(request.args.get("id"))
    return jsonify({"Message": message})
