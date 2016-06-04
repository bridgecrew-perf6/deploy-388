# -*- coding: utf-8 -*- 
__author__ = 'Administrator'

from . import ctrl
from flask import render_template, request, url_for
from app.models import Project, Environ, Server, Task
from app.business.project import ProjectBusiness
from app.business.task import TaskBusiness
from app.business.git import Git
from app.business.dbsession import DBSession
from app.utils.result import Result


@ctrl.route("/task/index/")
@ctrl.route("/task/")
@ctrl.route("/task/list/")
def task_list():
	env_list = Environ.query.all()
	server_list = Server.query.all()
	task_list = Task.query.all()
	task_status_desc_map = TaskBusiness.TASK_STATUS_DESC_MAP
	task_action_id_desc_map = TaskBusiness.TASK_ACTION_ID_DESC_MAP

	task_status_create = TaskBusiness.TASK_STATUS_CREATE
	task_status_review_success = TaskBusiness.TASK_STATUS_REVIEW_SUCCESS
	task_status_review_reject = TaskBusiness.TASK_STATUS_REVIEW_REJECT
	task_status_deploy_success = TaskBusiness.TASK_STATUS_DEPLOY_SUCCESS
	task_status_deploy_fail = TaskBusiness.TASK_STATUS_DEPLOY_FAIL
	task_action_id_deploy = TaskBusiness.TASK_ACTION_ID_DEPLOY
	task_action_id_rollback = TaskBusiness.TASK_ACTION_ID_ROLLBACK

	return render_template("task/list.html", task_list=task_list,
						   task_status_desc_map=task_status_desc_map,
						   task_action_id_desc_map=task_action_id_desc_map,
						   task_status_create=task_status_create,
						   task_status_review_success=task_status_review_success,
						   task_status_review_reject=task_status_review_reject,
						   task_status_deploy_success=task_status_deploy_success,
						   task_status_deploy_fail=task_status_deploy_fail,
						   task_action_id_deploy=task_action_id_deploy,
						   task_action_id_rollback=task_action_id_rollback,
						   )


@ctrl.route("/task/choose/")
def task_choose():
	project_list = Project.query.filter_by(status=ProjectBusiness.PROJECT_STATUS_ON)
	env_list = Environ.query.all()
	server_list = Server.query.all()
	return render_template("task/choose.html",
						   project_list=project_list,
						   env_list=env_list, server_list=server_list)


@ctrl.route("/task/submit/project_id/<project_id>/env_id/<env_id>", methods=["GET"])
def task_submit(project_id=None, env_id=None):
	if (project_id is None or project_id == "" or env_id is None or env_id == ""):
		return "error"
	project = Project.query.filter_by(id=project_id).first()
	if (project is None or project.status == ProjectBusiness.PROJECT_STATUS_OFF):
		return "no such project"
	git = Git(project)
	git.updateRepo()
	branch_list = git.getBranch()
	commit_list = git.getCommit()

	project = Project.query.filter_by(id=project_id).first()
	env = Environ.query.filter_by(id=env_id).first()

	return render_template("task/submit.html",
						   project=project, env=env,
						   branch_list=branch_list, commit_list=commit_list)


@ctrl.route("/task/do_submit", methods=["POST"])
def task_do_submit():
	method = request.method
	if (method == "POST"):

		form = request.form
		project_id = form.get("project_id", "").strip()
		env_id = form.get("env_id", "").strip()
		task_title = form.get("task_title").strip()
		branch = form.get("branch").strip()
		commit = form.get("commit").strip()

		task_count = Task.query.filter_by(project_id=project_id, env_id=env_id).count()
		roll_back = "no"
		if (task_count > 0):
			roll_back = "yes"

		task = Task()
		task.task_title = task_title.strip()
		task.branch_id = branch
		task.commit_id = commit
		task.user_id = 0
		task.project_id = project_id
		task.env_id = env_id
		task.rollback_enable = roll_back
		task.status = "create"
		task.action_id = "deploy"

		DBSession.save(task)

		return Result("succ", 0, url_for(".project_list")).getIframeResponse()
	else:
		return Result("error", 1)


@ctrl.route("/task/delete")
def task_delete():
	pass


@ctrl.route("/task/toggleStatus/task_id/<task_id>/status/<status>", methods=["GET"])
def task_toggle_status(task_id=None, status=None):
	if (task_id is None or status is None):
		return Result("fail", 1, url_for("ctrl.task_list")).getJson()
	task = Task.query.filter_by(id=task_id).first()
	task.status = status
	DBSession.save(task)

	return Result("succ", 0, url_for("ctrl.task_list")).getJson()


@ctrl.route("/task/deploy/task_id/<task_id>", methods=["GET", "POST"])
def task_deploy(task_id=None):
	pass


@ctrl.route("/task/rollback/task_id/<task_id>", methods=["GET", "POST"])
def task_rollback(task_id=None):
	pass
