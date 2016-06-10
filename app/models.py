# -*- coding: utf-8 -*- 
__author__ = 'Administrator'

from app import db

class User(db.Model):
	__tablename__="user"
	id=db.Column(db.INTEGER,primary_key=True)
	user_email=db.Column(db.VARCHAR(100),index=True,nullable=False,unique=True)
	user_name=db.Column(db.VARCHAR(20),nullable=True)
	user_password=db.Column(db.VARCHAR(100),nullable=False)
	is_admin=db.Column(db.Enum("no","yes"),nullable=False)

	def __repr__(self):
		return "<table %s>" % self.id

class Project(db.Model):
	__tablename__ = "project"
	id = db.Column(db.INTEGER, primary_key=True)
	project_no=db.Column(db.VARCHAR(50),index=True,nullable=True)
	project_name = db.Column(db.VARCHAR(50))
	project_description=db.Column(db.VARCHAR(200),nullable=True)
	repo_type = db.Column(db.Enum("svn","git"),default="git")
	repo_url = db.Column(db.VARCHAR(200))
	status = db.Column(db.Enum("on","off"),default="on")
	deploy_from = db.Column(db.VARCHAR(200))
	exclude = db.Column(db.Text)
	release_user = db.Column(db.VARCHAR(50))
	deploy_to = db.Column(db.VARCHAR(200))
	release_to = db.Column(db.VARCHAR(200))
	review = db.Column(db.Enum("on","off"),default="on")

	def __repr__(self):
		return "<table %s>" % self.id

class Environ(db.Model):
	__tablename__="environ"
	id=db.Column(db.INTEGER,primary_key=True)
	env_no=db.Column(db.VARCHAR(20),index=True,nullable=True)
	env_name=db.Column(db.VARCHAR(50))
	env_description=db.Column(db.VARCHAR(200),nullable=True,default="")
	env_ip=db.Column(db.VARCHAR(20),nullable=True)

	def __repr__(self):
		return "<table %s>" % self.id

class Server(db.Model):
	__tablename__="server"
	id=db.Column(db.INTEGER,primary_key=True)
	server_no=db.Column(db.VARCHAR(20),nullable=True,index=True)
	server_name=db.Column(db.VARCHAR(20),nullable=True,default="")
	server_ip=db.Column(db.VARCHAR(20))
	env_id=db.Column(db.INTEGER,index=True)
	project_id=db.Column(db.INTEGER,index=True)

	def __repr__(self):
		return "<table %s>" % self.id

class Task(db.Model):
	__tablename__="task"
	id=db.Column(db.INTEGER,primary_key=True)
	task_title=db.Column(db.VARCHAR(50),nullable=False)
	branch_id=db.Column(db.VARCHAR(50),nullable=False)
	commit_id=db.Column(db.VARCHAR(200),nullable=False)
	user_id=db.Column(db.INTEGER,nullable=True)
	project_id=db.Column(db.INTEGER,index=True)
	env_id=db.Column(db.INTEGER,index=True)
	link_id=db.Column(db.VARCHAR(100))
	ex_link_id=db.Column(db.VARCHAR(100))
	status=db.Column(db.Enum("create","review_success","review_reject","deploy_success","deploy_fail"))
	rollback_enable=db.Column(db.Enum("yes","no"))
	action_id=db.Column(db.Enum("deploy","rollback"))
	create_time=db.Column(db.DATETIME)

	def __repr__(self):
		return "<table %s>" % self.id

