# -*- coding: utf-8 -*- 
__author__ = 'Administrator'

from .command import Command


class Svn(Command):
	def updateRepo(self, branch="trunk"):
		pass

	def runLocalCommand(self):
		pass

	def runRemoteCommand(self):
		pass

	def getBranch(self):
		pass

	def getDeployFromAbsPath(self):
		pass
