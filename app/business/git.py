# -*- coding: utf-8 -*- 
__author__ = 'Administrator'

from command import Command
import os
from os import sep, path
from gittle import Gittle

class Git(Command):

	def updateRepo(self, branch="master",commit_id=None):

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
				if(commit_id is None):
					repo.pull(branch_name=branch)
				else:
					repo.checkout_all(commit_sha=commit_id)
			except Exception, e:
				return (2, e)
		else:
			try:
				repo = Gittle.clone(repo_url, git_dir, None, True)
				if(commit_id is None):
					repo.pull(branch_name=branch)
				else:
					repo.checkout_all(commit_sha=commit_id)
			except Exception, e:
				return (3, e)

		return (0, "update repo success")

	def getBranch(self):
		repo = Gittle(self.getDeployFromAbsPath())
		return repo.branches

	def getCommit(self):
		repo = Gittle(self.getDeployFromAbsPath())
		return repo.commit_info(start=0, end=20)
