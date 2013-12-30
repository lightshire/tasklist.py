# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1388331245.36813
_enable_loop = True
_template_filename = u'/home/lightshire/todolist.py/application/views/dashboard/task_list.html'
_template_uri = u'/dashboard/task_list.html'
_source_encoding = 'ascii'
from whirlwind.view.filters import Filters, Cycler
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<div class="panel panel-danger">\n\t  <div class="panel-heading">\n\t\t\t<h3 class="panel-title"><span class="glyphicon glyphicon-list-alt"></span>&nbsp;Current Task List</h3>\n\t  </div>\n\t  <div class="panel-body">\n\t\t\tPanel content\n\t  </div>\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


