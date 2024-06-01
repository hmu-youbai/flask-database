import os
import click
import json
from flask import Flask
from flask_bootstrap import Bootstrap4
from demo.blueprint.hppied import hppied
from demo.blueprint.search import search,db
from demo.blueprint.download import download
from demo.blueprint.help import help
from demo.blueprint.about import about
from flask_sqlalchemy import SQLAlchemy





def create_app(config_name=None):
    app = Flask('demo')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase22.db'  # 或其他数据库URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    bootstrap = Bootstrap4()
    bootstrap.init_app(app)

    app.register_blueprint(hppied)
    app.register_blueprint(search)
    app.register_blueprint(download)
    app.register_blueprint(help)
    app.register_blueprint(about)
    return app
