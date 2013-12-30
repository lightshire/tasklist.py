# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1388330878.499673
_enable_loop = True
_template_filename = u'/home/lightshire/todolist.py/application/views/dashboard/new_project.html'
_template_uri = u'/dashboard/new_project.html'
_source_encoding = 'ascii'
from whirlwind.view.filters import Filters, Cycler
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<div class="panel panel-info">\n\t  <div class="panel-heading">\n\t\t\t<h3 class="panel-title"><span class="glyphicon glyphicon-floppy-disk"></span>&nbsp;Create New Project</h3>\n\t  </div>\n\t  <div class="panel-body">\n\t\t\t<form action="/projects/create" method="post">\n\t\t\t\t<input type="hidden" name="redirect_url" value="/dashboard" />\n\t\t\t\t<div class="form-group">\n\t\t\t\t\t<label for="project_name">Project Name</label>\n\t\t\t\t\t<input type="text" name="project_name" id="project_name" placeholder="Enter the project Name here" class="form-control"/>\n\t\t\t\t</div>\n\t\t\t\t<div class="form-group">\n\t\t\t\t\t<label for="project_desc">Project Description</label>\n\t\t\t\t\t<textarea type="text" name="project_desc" id="project_desc" placeholder="Enter the project Description" class="form-control"></textarea>\n\t\t\t\t</div>\n\t\t\t\t<div class="form-group">\n\t\t\t\t\t<button class="btn btn-info pull-right" type="Submit">Save</button>\n\t\t\t\t</div>\n\t\t\t</form>\n\t  </div>\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


