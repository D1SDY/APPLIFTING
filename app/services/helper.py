from flask import Response, json, current_app
import requests
from app.models.Product import Product
from app.models.Offer import Offer
from app.routes import GET_NEW_OFFERS_ENDPOINT
from app.scheduler import scheduler


def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )


def make_post_call(url: str, data: str):
    return requests.post(current_app.config.get("APPLIFTING_BASE_URL").format(url),
                         data=data,
                         headers={'Bearer': current_app.config["API_TOKEN"]})


def make_get_call(url: str):
    return requests.get(current_app.config.get("APPLIFTING_BASE_URL").format(url),
                        headers={'Bearer': current_app.config["API_TOKEN"]})


@scheduler.task("interval", id="do_get_new_offers", minutes=1, misfire_grace_time=None)
def get_new_offers():
    products = Product.get_all_products()
    print("Retrieving updates from Applifting Offer ms")
    for product in products:
        url = GET_NEW_OFFERS_ENDPOINT.format(product.id)
        r = requests.get(url=scheduler.app.config.get("APPLIFTING_BASE_URL").format(url),
                         headers={'Bearer': scheduler.app.config["API_TOKEN"]})
        r_array = json.loads(r.text)
        for offer in r_array:
            data = json.loads(json.dumps(offer))
            offer_obj = Offer.get_single_offer(offer.get('id'))
            if offer_obj is None:
                offer_obj = Offer(data)
                offer_obj.product_id = product.id
                offer_obj.save()
            else:
                offer_obj.update(data)
