# -*- coding: utf-8 -*- 
__author__ = 'Administrator'

from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from app import login_manager

@login_manager.user_loader
def login(id):
	return UserBusiness.query.filter_by(id=int(id)).first()


class UserBusiness(User):

	IS_ADMIN_YES="yes"
	IS_ADMIN_NO="no"


	@property
	def password(self):
		raise AttributeError("password is not a  readable attribute")

	@password.setter
	def password(self, password):
		self.user_password = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.user_password, password)

	@property
	def is_authenticated(self):
		return  True

	@property
	def is_active(self):
		return  True
	@property
	def is_anonymous(self):
		return  False

	def get_id(self):
		return self.id

	def check_is_admin(self):
		return self.is_admin==UserBusiness.IS_ADMIN_YES
