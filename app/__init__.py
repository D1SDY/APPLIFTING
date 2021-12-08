import json
import os
import requests
from flask import Flask
from app.models import db
from .scheduler import scheduler
from app.routes.ProductRoutes import product_api
from app.routes.UserRoutes import user_api
from dotenv import load_dotenv
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI="sqlite:///instance/applifting.sqlite",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SCHEDULER_API_ENABLED=True,
        SCHEDULER_TIMEZONE="Europe/Prague",
        SCHEDULER_JOBSTORES={
            "default": SQLAlchemyJobStore(url="sqlite:///app/instance/jobs.sqlite")
        },
        JWT_SECRET_KEY="AppliftingJWT",


    )
    load_dotenv()
    API_TOKEN = os.environ.get('API_TOKEN')
    APPLIFTING_BASE_URL = os.environ.get('APPLIFTING_BASE_URL')
    if API_TOKEN is None:
        r = requests.post(APPLIFTING_BASE_URL.format('auth')).text
        access_token_env = "\nAPI_TOKEN={0}".format(json.loads(r).get('access_token'))
        with open('app/.env', "a") as f:
            f.write(access_token_env)

    db.init_app(app)
    db.app = app
    db.create_all()
    jwt = JWTManager(app)

    with app.app_context():
        app.register_blueprint(product_api)
        app.register_blueprint(user_api)
        app.config["API_TOKEN"] = API_TOKEN
        app.config["APPLIFTING_BASE_URL"] = APPLIFTING_BASE_URL

    scheduler.init_app(app)
    scheduler.start()

    @app.route('/')
    def hello():
        return "Hello, World"

    return app
