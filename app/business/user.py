# -*- coding: utf-8 -*- 
__author__ = 'Administrator'

from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from app import login_manager

class UserBusiness(User):
	@property
	def password(self):
		raise AttributeError("password is not a  readable attribute")

	@password.setter
	def password(self, password):
		self.user_password = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.user_password, password)

	def is_authenticated(self):
		return  True

	def is_active(self):
		return  True

	def is_anonymous(self):
		return  False

	def get_id(self):
		return self.user_email

	@login_manager.user_loader
	@staticmethod
	def login(user_email):
		return UserBusiness.query.filter_by(user_email=user_email).first()
