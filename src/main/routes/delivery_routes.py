from flask import Blueprint, jsonify, request

from src.main.http_types.http_request import HttpRequest

delivery_routes_bp = Blueprint('delivery_routes', __name__)

@delivery_routes_bp.route('/delivery/order', methods=['POST'])
def registry_order():
    http_request = request.json

    #levar o http_request para a lógica
    #lógica retorna a response
    

    return jsonify({"hello": "world"}), 200