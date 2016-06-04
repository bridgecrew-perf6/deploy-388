# -*- coding: utf-8 -*- 
__author__ = 'Administrator'


class Util:
	@staticmethod
	def _arrayGroup(list, key):
		if (type(list) != "list"):
			raise ValueError
