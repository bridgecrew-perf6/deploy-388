# -*- coding: utf-8 -*- 
__author__ = 'Administrator'

from .git import Git
from .svn import Svn


class Repo:
	REPO_TYPE_GIT = "git"
	REPO_TYPE_SV = "svn"

	@staticmethod
	def getRepo(project):
		type = project.repo_type

		if (type == Repo.REPO_TYPE_GIT):
			return Git(project)
		elif (type == Repo.REPO_TYPE_SV):
			return Svn(project)
		else:
			raise ValueError, "repo type must be svn or git"
