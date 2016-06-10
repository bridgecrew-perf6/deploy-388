# -*- coding: utf-8 -*- 
__author__ = 'Administrator'

from app.models import Task


class TaskBusiness():
	PROJECT_STATUS_ON = "on"
	PROJECT_STATUS_OFF = "off"

	TASK_STATUS_CREATE = "create"
	TASK_STATUS_REVIEW_SUCCESS = "review_success"
	TASK_STATUS_REVIEW_REJECT = "review_reject"
	TASK_STATUS_DEPLOY_SUCCESS = "deploy_success"
	TASK_STATUS_DEPLOY_FAIL = "deploy_fail"

	TASK_ACTION_ID_DEPLOY = "deploy"
	TASK_ACTION_ID_ROLLBACK = "rollback"

	TASK_STATUS_DESC_MAP = {
		TASK_STATUS_CREATE: u"新建",
		TASK_STATUS_REVIEW_SUCCESS: u"审核通过",
		TASK_STATUS_REVIEW_REJECT: u"审核未通过",
		TASK_STATUS_DEPLOY_SUCCESS: u"发布成功",
		TASK_STATUS_DEPLOY_FAIL: u"发布失败",
	}

	TASK_ACTION_ID_DESC_MAP = {
		TASK_ACTION_ID_DEPLOY: u"发布",
		TASK_ACTION_ID_ROLLBACK: u"回滚"
	}
