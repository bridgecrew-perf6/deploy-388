# -*- coding: utf-8 -*- 
__author__ = 'Administrator'

from abc import ABCMeta, abstractmethod
from paramiko import SSHClient,RSAKey
from os import path,sep
from app.utils.rsync import Rsync

class Command:
	__metaclass__ = ABCMeta

	def __init__(self, project):
		self.project = project

	@abstractmethod
	def updateRepo(self, branch,commit_id=None):
		pass

	@abstractmethod
	def getBranch(self):
		pass

	@abstractmethod
	def getCommit(self):
		pass

	def getDeployFromAbsPath(self):
		deploy_from = self.project.deploy_from
		project_no = self.project.project_no
		git_dir = deploy_from.rstrip(sep) + sep + project_no.rstrip(sep)
		return git_dir

	def getDeployToAbsPath(self):
		deploy_to=self.project.deploy_to
		project_no=self.project.project_no
		deploy_to_path=deploy_to.rstrip(sep)+sep+project_no.rstrip(sep)
		return  deploy_to_path

	def syncDir(self,remote_address,exclude_file_or_dir=None):
		remote_user=self.project.release_user
		deploy_from_abs_path=self.getDeployFromAbsPath()
		deploy_to_abs_path=self.getDeployToAbsPath()
		sync=Rsync(remote_user,remote_address)
		return sync.syncDir(deploy_from_abs_path,deploy_to_abs_path,exclude_file_or_dir)

	def connectRemoteAddress(self,remote_user,remote_address,key_file):
		ssh=SSHClient()
		ssh.load_system_host_keys()
		private_key=path.expanduser("~/.ssh/id_rsa")
		key=RSAKey.from_private_key_file(private_key)
		ssh.connect(username=remote_user,hostname=remote_address,pkey=key)
		return ssh

	def doRelease(self):
		pass
	def doRollback(self):
		pass