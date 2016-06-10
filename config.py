# -*- coding: utf-8 -*- 
__author__ = 'Administrator'


class Config:

	SECRET_KEY = "hard to guess"
	SQLALCHEMY_DATABASE_URI = "mysql://jidan:zhuan1234@jidan.cpmjiidkwboh.us-west-2.rds.amazonaws.com/deploy"

	MAIL_SERVER = "smtp.qq.com"
	MAIL_PORT = "465"
	MAIL_USERNAME = "394777474@qq.com"
	MAIL_PASSWORD = "zhuan123456"

	@staticmethod
	def init_app(app):
		pass


class DevelopConfig(Config):
	DEBUG = True


class TestConfig(Config):
	TEST = True


class AlphaConfig(Config):
	pass


class ProductConfig(Config):
	pass


config = {
	"dev": DevelopConfig,
	"test": TestConfig,
	"alpha": AlphaConfig,
	"product": ProductConfig,

	"default": DevelopConfig,
}
