from whirlwind.core.request import BaseRequest
from whirlwind.db.mongo import Mongo
from application.models.user import User
from application.models.project import Project
import datetime, hashlib
from tornado.web import authenticated
from whirlwind.view.decorators import route

@route('/projects/create')
class SaveProjectController(BaseRequest):
	def post(self):
		current_user	= self.get_current_user()
		project_name 	= self.get_argument("project_name",None)
		project_desc 	= self.get_argument("project_desc",None)
		redirect 		= self.get_argument("redirect_url",None)
		
		if not current_user:
			self.flash.error = "Please login to continue"
			self.redirect("/")

		if not project_name or not project_desc:
			self.flash.error = "Please enter the <strong>Project Name</strong> and the <strong>Project Description</strong>"
			
			if not redirect:
				self.redirect("/projects/create")
			else:
				self.redirect(redirect)

		project = Project.instance(project_name, project_desc, current_user._id)
		Project.save(project)

		self.flash.success = "You have successfully saved a project"

		if not redirect:
			self.redirect("/projects/create")
		else:
			self.redirect(redirect)

