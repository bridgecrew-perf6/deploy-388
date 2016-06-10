# -*- coding: utf-8 -*- 
__author__ = 'Administrator'

from . import ctrl
from flask import request, render_template, url_for
from app.business.dbsession import DBSession
from app.utils.result import Result
from app.models import Server, Environ, Project
from app.business.server import ServerBusinese
from flask_login import login_required


@ctrl.route("/server/")
@ctrl.route("/server/list/")
@ctrl.route("/server/index/")
@login_required
def server_list():
	server_list = Server.query.all()
	return render_template("server/list.html", server_list=server_list)


@ctrl.route("/server/edit/<server_id>/", methods=["GET", "POST"])
@login_required
def server_edit(server_id=None):
	method = request.method
	server_id = request.args.get("evn_id", "").strip()
	if (method == "POST"):
		form = request.form
		server_no = form.get("server_no", "")
		server_name = form.get("server_name")
		server_ip = form.get("server_ip", "")
		project_id = form.get("project_id", "")
		env_id = form.get("env_id", "")

		model = Server()
		if (server_id):
			query_model = Server.query.filter_by(id=server_id).first()
			if (query_model is not None):
				model = query_model

		for item in form:
			item_val = form.get(item, "")
			print  item, item_val
			if (hasattr(model, item)):
				model.__setattr__(item, item_val)

		DBSession.save(model)
		return Result("succ", 0, url_for(".server_list")).getIframeResponse()

	else:
		if (server_id):
			server = Server.query.filter_by(id=server_id).first()
		else:
			server = Server()
		project_list = Project.query.all()
		env_list = Environ.query.all()

		print server_list, env_list
		return render_template("server/edit.html", server=server, project_list=project_list, env_list=env_list)
