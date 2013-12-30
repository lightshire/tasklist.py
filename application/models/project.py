from mongokit import *
import datetime
import hashlib, hmac, base64, re
from whirlwind.db.mongo import Mongo
from tornado import options
from config.settings import *
def normalize(prepped_string):
	if not prepped_string:
		return None

	name = prepped_string.strip().lower()
	name = name.replace(".", "")
	name = name.replace("$", "")
	return name;

@Mongo.db.connection.register
class Project(Document):

	__collection__ 	= 'projects'
	__database__ 	= db_name
	structure = {
					# '_id'			:	unicode,
					'project_name' 	: 	unicode,
					'project_desc' 	: 	unicode,
					'tasks' 		:   list,
					'user_owner' 	: 	unicode 	
				}
	use_dot_notation = True

	@staticmethod
	def normalize(project_name):
		return normalize(project_name)

	@staticmethod
	def instance(project_name, project_desc, user_owner):
		project = Project()
		project.tasks = []
		project.project_name = project_name
		project.project_desc = project_desc
		project.user_owner 	 = user_owner
		return project

	@staticmethod
	def save(project):
		Mongo.db.ui.projects.insert(project) 

	@staticmethod
	def all():
		return connection.Project().find()
