# -*- coding: utf-8 -*- 
__author__ = 'Administrator'


from paramiko import Transport,RSAKey,SFTPClient
import os

host="54.187.91.18"
port=22

private_key_file=os.path.expanduser("~/.ssh/id_rsa")
key=RSAKey.from_private_key_file(private_key_file)


t=Transport((host,port))
t.connect(username="ec2-user",pkey=key)

sftp=SFTPClient.from_transport(t)
try:
	sftp.put("/data/websites/test/a.php","/data/websites/")
except Exception,e:
	print(e)

sftp.close()
t.close()

