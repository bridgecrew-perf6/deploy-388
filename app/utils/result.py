# -*- coding: utf-8 -*- 
__author__ = 'Administrator'

import json


class Result():
	def __init__(self, message, code=1, jum_url="", **kwargs):
		self.message = message
		self.code = int(code)
		self.jum_url = jum_url
		self.data = kwargs

	def isSuccess(self):
		return 0 == self.code

	def getCode(self):
		return self.code

	def setCode(self, code):
		self.code = code

	def getMessage(self):
		return self.message

	def setMessage(self, message):
		self.message = message

	def setData(self, **kwargs):
		self.data = kwargs

	def getData(self):
		return self.data

	def setDataItem(self, key, value):
		self.data[key] = value

	def getDataItem(self, key):
		if (key in self.data):
			return self.data[key]
		else:
			return ""

	def setJumpUrl(self, jum_url):
		self.jum_url = jum_url

	def getJumpUrl(self):
		return self.jum_url

	def getList(self):
		return dict({"code": self.getCode(), "message": self.getMessage(), "jump_url": self.getJumpUrl()}, **self.data)

	def getJson(self):
		return json.dumps(self.getList())

	def getJsonP(self):
		pass

	def getIframeResponse(self):
		html = """<!doctype html>
				<html lang="en">
				<head>
				<meta charset="UTF-8" />
				<title></title>
				<script>
				var frame = null;
				try {
					frame = window.frameElement;
				} catch(ex){
					try {
						document.domain = location.host.replace(/^[\w]+\./, '');
						frame = window.frameElement;
					} catch(ex){
						if(window.console){
							console.log("i try twice to cross domain. sorry, i m give up...");
						}
					}
				};
				</script>
				<script>
				frame._callback(""" + str(self.getList()) + """);
				</script>
				</head>
				<body></body>
				</html>"""
		return html

	def __str__(self):
		return self.getIframeResponse()
