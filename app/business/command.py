# -*- coding: utf-8 -*- 
__author__ = 'Administrator'

from abc import ABCMeta, abstractmethod


class Command:
	__metaclass__ = ABCMeta

	def __init__(self, project):
		self.project = project

	@abstractmethod
	def updateRepo(self, branch):
		pass

	@abstractmethod
	def runLocalCommand(self):
		pass

	@abstractmethod
	def runRemoteCommand(self):
		pass

	@abstractmethod
	def getBranch(self):
		pass

	@abstractmethod
	def getCommit(self):
		pass

	@abstractmethod
	def getDeployFromAbsPath(self):
		pass
