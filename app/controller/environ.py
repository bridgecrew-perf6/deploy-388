# -*- coding: utf-8 -*- 
__author__ = 'Administrator'

from . import ctrl
from flask import request, render_template, url_for
from app.models import Environ
from app.business.dbsession import DBSession
from app.utils.result import Result
from flask_login import login_required


@ctrl.route("/env/")
@ctrl.route("/env/list/")
@ctrl.route("/env/index/")
@login_required
def env_list():
	env_list = Environ.query.all()
	print request.__dict__
	print(request.path)
	return render_template("environ/list.html", env_list=env_list)


@ctrl.route("/env/edit/<env_id>/", methods=["GET", "POST"])
@login_required
def env_edit(env_id=None):
	method = request.method
	env_id = request.args.get("evn_id", "").strip()
	if (method == "POST"):
		form = request.form
		if (env_id == ""):
			env_id = form.get("env_id", "").strip()

		env_no = form.get("env_no", "").strip
		env_name = form.get("env_name", "").strip()
		env_description = form.get("env_description", "").strip()
		env_ip = form.get("env_ip", "").strip()

		model = Environ()
		if (env_id != ""):
			query_evn = Environ.query.filter_by(id=env_id).first()
			if (query_evn is not None):
				model = query_evn

		for item in form:
			item_val = form.get(item, "")
			if (hasattr(model, item)):
				model.__setattr__(item, item_val)

		DBSession.save(model)
		return Result("succ", 0, url_for('ctrl.env_list')).getIframeResponse()

	else:
		if (env_id != ""):
			environ = Environ.query.filter_by(env_id=env_id).first()
		else:
			environ = None
		return render_template("environ/edit.html", environ=environ)


@ctrl.route("/evn/delete/<env_id>")
@login_required
def env_delete(env_id=None):
	pass
