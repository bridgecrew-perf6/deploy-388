# -*- coding: utf-8 -*- 
__author__ = 'Administrator'

import commands

class Rsync():

	def __init__(self,remote_user,remote_address):
		self.remote_user=remote_user
		self.remote_address=remote_address

	def syncDir(self,local_dir,remote_dir=None,exclude_file_or_dir=None):
		if(remote_dir is None):
			remote_dir=local_dir

		if(exclude_file_or_dir is not None):
			cmd="rsync -avzP %s --exclude=%s %s@%s:%s" % (local_dir,exclude_file_or_dir,
														  self.remote_user,
											  self.remote_address,remote_dir)
		else:
			cmd="rsync -avzP %s  %s@%s:%s" % (local_dir,self.remote_user,
											  self.remote_address,remote_dir)

		return commands.getstatusoutput(cmd)

	def syncFile(self):
		pass

	def syncDirList(self):
		pass


	def syncFileList(self):
		pass