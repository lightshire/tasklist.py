# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1388333288.840316
_enable_loop = True
_template_filename = u'/home/lightshire/todolist.py/application/views/dashboard/my_project_list.html'
_template_uri = u'/dashboard/my_project_list.html'
_source_encoding = 'ascii'
from whirlwind.view.filters import Filters, Cycler
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<div class="panel panel-info">\n\t  <div class="panel-heading">\n\t\t\t<h3 class="panel-title">My Project List</h3>\n\t  </div>\n\t  <div class="panel-body">\n\t\t\t<table class="table-hover table-condensed table table-responsive">\n\t\t\t\t<thead>\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<th><span class="glyphicon glyphicon-cog"></span>&nbsp;Project Name</th>\n\t\t\t\t\t\t<th><span class="glyphicon glyphicon-bell"></span>&nbsp;Status</th>\n\t\t\t\t\t\t<th><span class="glyphicon glyphicon-list-alt"></span>&nbsp;Number of Tasks</th>\n\t\t\t\t\t\t<th>&nbsp;</th>\n\t\t\t\t\t</tr>\n\t\t\t\t</thead>\n\t\t\t\t<tbody>\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td>TodoList.Py Project (GWD)</td>\n\t\t\t\t\t\t<td><span class="label label-success">Active</span></td>\n\t\t\t\t\t\t<td><span class="label label-info">22</span></td>\n\t\t\t\t\t</tr>\n\t\t\t\t</tbody>\n\t\t\t</table>\n\t  </div>\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


