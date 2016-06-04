# -*- coding: utf-8 -*-
import flask

__author__ = 'Administrator'

from . import ctrl
from flask import render_template, url_for
from flask import request
from app.models import Project
from app.business.dbsession import DBSession
from app.utils.result import Result
from app.business.repo import Repo
from flask_login import login_required


@login_required
@ctrl.route("/project/")
@ctrl.route("/project/list/")
@ctrl.route("/project/index/")
def project_list():
	project_list = Project.query.all()
	return render_template("project/list.html", project_list=project_list)


@ctrl.route('/project/edit/<project_id>', methods=["GET", "POST"])
def project_edit(project_id=None):
	method = request.method
	project_id = project_id.strip()

	if (method == "POST"):

		form = request.form
		project_no = form.get("project_no", "")
		project_name = form.get("project_name", "")
		repo_type = form.get("repo_type", "git")
		repo_url = form.get("repo_url")
		status = form.get("status", "on")
		deploy_from = form.get("deploy_from", "")
		exclude = form.get("exclude", "")
		release_user = form.get("release_user", "")
		deploy_to = form.get("deploy_to", "")
		release_to = form.get("release_to", "")
		review = form.get("review", "")

		model = Project()
		if (project_id is None or project_id == ""):
			query_project = Project.query.filter_by(id=project_id).first()
			if (query_project is not None):
				model = query_project()

		for item in form:
			item_val = form.get(item, "")
			if (hasattr(model, item)):
				model.__setattr__(item, item_val)

		DBSession.save(model)
		return Result("succ", 0, url_for(".project_list")).getIframeResponse()
	else:
		return render_template("project/edit.html", project_id=None)


@ctrl.route('/project/delete/<project_id>', methods=["GET"])
def project_delete(project_id=None):
	pass


@ctrl.route("/project/toggle/<project_id>", methods=["GET"])
def project_toggle(project_id=None):
	if (project_id is None):
		return Result("project cant be none", 1).getIframeResponse()
	project = Project.query.filter_by(project_id=project_id).first()
	if (project is None):
		return Result("no such project", 1)
	project.status = int(not project.status)
	DBSession.save(project)
	return Result("succ", 0, url_for(".project_list"))


@ctrl.route("/project/environ/<project_id>")
def project_environ(project_id=None):
	pass


@ctrl.route("/project/check/<project_id>")
def project_check(project_id=None):
	if (project_id is None or project_id == ""):
		return Result("project cant be none", 1).getJson()
	project = Project.query.filter_by(project_id=project_id).first()
	if (project is None):
		return Result("no such project", 1).getJson()
	repo = Repo.getRepo(project)
	data = repo.updateRepo()

	print(data)

	return "==="
