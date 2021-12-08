from flask import Blueprint, request
from marshmallow import ValidationError
from . import REGISTER_PRODUCT_ENDPOINT
from ..schema.ProductSchema import ProductSchema
from ..models.Product import Product
from app.services.helper import custom_response, make_post_call
from flask_jwt_extended import jwt_required

product_api = Blueprint('product_api', __name__, url_prefix="/product")
product_schema = ProductSchema()


@product_api.route('/create', methods=['POST'])
@jwt_required()
def create():
    req_data = request.get_json()
    try:
        data = product_schema.load(req_data)
    except ValidationError as error:
        return custom_response(error, 400)
    post = Product(data)
    post.save()
    data = product_schema.dump(post)
    r = make_post_call(REGISTER_PRODUCT_ENDPOINT, data)
    return custom_response(data, r.status_code)


@product_api.route('/<int:product_id>', methods=['GET'])
@jwt_required()
def get_one(product_id):
    post = Product.get_single_product(product_id)
    if not post:
        return custom_response({'error': 'post not found'}, 404)
    data = product_schema.dump(post)
    return custom_response(data, 200)


@product_api.route('/<int:product_id>', methods=['PUT'])
@jwt_required()
def update(product_id):
    req_data = request.get_json()
    post = Product.get_single_product(product_id)
    if not post:
        return custom_response({'error': 'post not found'}, 404)
    try:
        data = product_schema.load(req_data, partial=True)
    except ValidationError as error:
        return custom_response(error, 400)
    post.update(data)
    data = product_schema.dump(post)
    return custom_response(data, 200)


@product_api.route('/<int:product_id>', methods=['DELETE'])
@jwt_required()
def delete(product_id):
    post = Product.get_single_product(product_id)
    if not post:
        return custom_response({'error': 'post not found'}, 404)
    post.delete()
    return custom_response({'message': 'deleted'}, 204)


@product_api.route('/get_all_offers/<int:product_id>', methods=['GET'])
@jwt_required()
def get_all_offers(product_id):
    post = Product.get_single_product(product_id)
    if not post:
        return custom_response({'error': 'post not found'}, 404)
    data = product_schema.dump(post)
    return custom_response({'offers': data['offers']}, 200)
