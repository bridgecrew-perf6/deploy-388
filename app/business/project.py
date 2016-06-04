# -*- coding: utf-8 -*- 
__author__ = 'Administrator'

from app.models import Project


class ProjectBusiness():
	PROJECT_STATUS_ON = "on"
	PROJECT_STATUS_OFF = "off"

	@staticmethod
	def getProjectName(project_id):
		project = Project.query.filter_by(id=project_id).frist()
		return project.project_name
