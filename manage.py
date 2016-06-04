# -*- coding: utf-8 -*- 
__author__ = 'Administrator'


from app import create_app,db
from flask_script import Manager,Shell
from flask_migrate import Migrate,MigrateCommand
from app.models import Project,Environ

app=create_app("dev")
manager=Manager(app)
migrate=Migrate(app,db)

def make_shell_content():
	return dict(app=app,db=db,project=Project,env=Environ)


manager.add_command("shell",Shell(make_context=make_shell_content))
manager.add_command("db",MigrateCommand)

if __name__ == "__main__":
	manager.run()