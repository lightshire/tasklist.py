# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1388185855.23985
_enable_loop = True
_template_filename = u'/home/lightshire/todolist.py/application/views/shared/header.html'
_template_uri = u'/shared/header.html'
_source_encoding = 'utf-8'
from whirlwind.view.filters import Filters, Cycler
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        is_logged_in = context.get('is_logged_in', UNDEFINED)
        current_user = context.get('current_user', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'<nav class="navbar navbar-default navbar-fixed-top" role="navigation">\n\t<div class="container">\n\t\t<div class="navbar-header">\n\t\t\t<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">\n\t\t\t\t<span class="sr-only">Toggle Navigation</span>\n\t\t\t\t<span class="icon-bar">&nbsp;</span>\n\t\t\t\t<span class="icon-bar">&nbsp;</span>\n\t\t\t\t<span class="icon-bar">&nbsp;</span>\n\t\t\t</button>\n\t\t\t<a class="navbar-brand" href="/"><img src="/static/images/logo-square.png" class=\'header-logo\'/>TodoList.py</a>\n\t\t</div>\n\t\t<div class="collapse navbar-collapse" id="navbar-collapse">\n')
        # SOURCE LINE 14
        if is_logged_in :
            # SOURCE LINE 15
            __M_writer(u'\t\t\t<ul class="nav navbar-nav navbar-left">\n\t\t\t\t<li>\n\t\t\t\t\t<a href="/dashboard/projects"><span class="glyphicon glyphicon-folder-open"></span>&nbsp;Projects</a>\n\t\t\t\t</li>\n\t\t\t\t<li>\n\t\t\t\t\t<a href="/dashboard/tasks"><span class="glyphicon glyphicon-wrench"></span>&nbsp;Tasks</a>\n\t\t\t\t</li>\n\n\t\t\t</ul>\n')
        # SOURCE LINE 25
        __M_writer(u'\t\t\t<ul class="nav navbar-nav navbar-right">\n')
        # SOURCE LINE 26
        if is_logged_in :
            # SOURCE LINE 27
            __M_writer(u'\t\t\t\t\t<li><a href="#"><span class="glyphicon glyphicon-user"></span>&nbsp;')
            __M_writer(unicode(current_user['_id']))
            __M_writer(u'</a></li>\n\t\t\t\t\t<li><a href="/logout"><span class="glyphicon glyphicon-log-out"></span>&nbsp;Log Out</a></li>\n')
            # SOURCE LINE 29
        else :
            # SOURCE LINE 30
            __M_writer(u'\t\t\t\t\t<li><a href="/login"><span class="glyphicon glyphicon-log-in"></span>&nbsp;Log In</a></li>\n\t\t\t\t\t<li><a href="/signup"><span class="glyphicon glyphicon-pencil"></span>&nbsp;Sign Up</a></li>\n')
        # SOURCE LINE 33
        __M_writer(u'\t\t\t</ul>\n\t\t</div>\n\t</div>\n</nav>')
        return ''
    finally:
        context.caller_stack._pop_frame()


