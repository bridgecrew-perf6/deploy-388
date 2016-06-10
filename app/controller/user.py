# -*- coding: utf-8 -*- 
__author__ = 'Administrator'

from . import ctrl
from flask import request, render_template, url_for,redirect
from app.utils.result import Result
from app.models import User
from app.business.user import UserBusiness
from app.business.dbsession import DBSession
from flask_login import login_user, login_required,logout_user


@ctrl.route("/")
@ctrl.route("/login", methods=["GET", "POST"])
def user_login():
	form_url = url_for("ctrl.user_login")
	method = request.method
	if (method == "POST"):
		form = request.form
		user_email = form.get("user_email", "").rstrip()
		user_password = form.get("user_password").rstrip()
		if (user_email == "" or user_password == ""):
			return Result("email or password error", 1).getIframeResponse()
		user_model = UserBusiness.query.filter_by(user_email=user_email).first()
		if (user_model is None):
			return Result("account has been exist", 1).getIframeResponse()
		verify = user_model.verify_password(user_password)
		if (verify is False):
			return Result("email or password error", 1).getIframeResponse()
		login_user(user_model,True)
		next=request.args.get("next","")
		if(next!=""):
			redirect(next)
		return Result("succ", 0, url_for("ctrl.task_list")).getIframeResponse()
	else:
		action = "login"
		return render_template("user/login.html", form_url=form_url, action=action)


@ctrl.route("/register", methods=["GET", "POST"])
def user_register():
	form_url = url_for("ctrl.user_register")
	method = request.method
	if (method == "POST"):
		form = request.form
		user_email = form.get("user_email", "").rstrip()
		user_password = form.get("user_password").rstrip()
		if (user_email == "" or user_password == ""):
			return Result("email or password error", 1).getIframeResponse()
		user_model = User.query.filter_by(user_email=user_email).first()
		if (user_model is not None):
			return Result("account has been exist", 1).getIframeResponse()
		user_model = UserBusiness()
		user_model.user_email = user_email
		user_model.password = user_password
		DBSession.save(user_model)

		return Result("succ", 0, form_url).getIframeResponse()
	else:
		action = "register"
		return render_template("user/register.html", form_url=form_url, action=action)


@ctrl.route("/logout", methods=["GET", "POST"])
@login_required
def user_logout():
	logout_user()
	return redirect(url_for("ctrl.user_login"))


@ctrl.route("/user/profile", methods=["GET", "POST"])
@login_required
def user_profile():
	return "hah "
