# -*- coding: utf-8 -*- 
__author__ = 'Administrator'

from flask import Blueprint

ctrl = Blueprint("ctrl", __name__)

from . import environ, project, task, user, views, server
