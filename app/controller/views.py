# -*- coding: utf-8 -*- 
__author__ = 'Administrator'

from . import ctrl


@ctrl.route("/")
@ctrl.route("/index")
def index():
	return "hello,deploy!"
