# -*- coding: utf-8 -*- 
__author__ = 'Administrator'

from command import Command
import os
from os import sep, path, system
import commands
from gittle import Gittle


class Git(Command):
	def updateRepo(self, branch="master"):

		repo_url = self.project.repo_url

		git_dir = self.getDeployFromAbsPath()
		if (path.exists(git_dir) is False):
			try:
				os.mkdir(git_dir)
			except OSError, e:
				return (1, "create %s failed" % git_dir)

		git_symbol = git_dir + sep + ".git"
		if (path.exists(git_symbol)):
			try:
				repo = Gittle(git_dir, origin_uri=repo_url)
				repo.pull(branch_name=branch)
			except Exception, e:
				return (2, e)
		else:
			try:
				repo = Gittle.clone(repo_url, git_dir, None, True)
			except Exception, e:
				return (3, e)
			try:
				repo.pull(branch_name=branch)
			except Exception, e:
				return (4, e)

		return (0, "update repo success")

	def runLocalCommand(self):
		pass

	def runRemoteCommand(self):
		pass

	def getBranch(self):
		repo = Gittle(self.getDeployFromAbsPath())
		return repo.branches

	def getCommit(self):
		repo = Gittle(self.getDeployFromAbsPath())
		return repo.commit_info(start=0, end=20)

	def getDeployFromAbsPath(self):
		deploy_from = self.project.deploy_from
		project_no = self.project.project_no

		git_dir = deploy_from.rstrip(sep) + sep + project_no.rstrip(sep)
		return git_dir
