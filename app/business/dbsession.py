# -*- coding: utf-8 -*- 
__author__ = 'Administrator'

from app import db


class DBSession:
	@staticmethod
	def save(model):
		db_session = db.session
		db_session.add(model)
		return db_session.commit()

	@staticmethod
	def delete(model):
		db_session = db.session
		db_session.delete(model)
		return db_session.commit()
