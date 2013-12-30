from whirlwind.core.request import BaseRequest
from whirlwind.db.mongo import Mongo
from tornado.web import authenticated
from whirlwind.view.decorators import route
from application.models.project import Project

@route('/')
class IndexHandler(BaseRequest):
	def get(self):
		#template context variables go in here
		current_user = self.get_current_user()
		#if not self.session['username']:
		if not current_user:
			template_values = {}		
			self.render_template('/site/index.html',**template_values)
		else:
			self.redirect('/dashboard')

@route('/dashboard')
class DashboardHandler(BaseRequest):
	def get(self):
		
		template_values = {
			'projects' : Project().all()
		}

		self.render_template('/dashboard/index.html', **template_values)
