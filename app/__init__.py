# -*- coding: utf-8 -*- 
__author__ = 'Administrator'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from config import Config
from flask_login import LoginManager

db = SQLAlchemy()

login_manager=LoginManager()
login_manager.session_protection="strong"
login_manager.login_view="ctrl.user_login"


def create_app(config_name):
	# 初始化APP
	app = Flask(__name__)

	curr_config = config[config_name]
	app.config.from_object(curr_config)
	Config.init_app(app)

	db.init_app(app)

	login_manager.init_app(app)

	from .controller import ctrl
	app.register_blueprint(ctrl)


	return app
