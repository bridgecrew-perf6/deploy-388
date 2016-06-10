# -*- coding: utf-8 -*- 
__author__ = 'Administrator'

from flask_mail import Message
from app import mail

def send_mail(to,subject):
	mesage=Message(subject=subject,recipients=[to],body="测试")
	return mail.send(mesage)