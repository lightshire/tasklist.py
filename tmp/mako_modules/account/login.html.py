# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1388187146.539407
_enable_loop = True
_template_filename = '/home/lightshire/todolist.py/application/views/account/login.html'
_template_uri = '/account/login.html'
_source_encoding = 'utf-8'
from whirlwind.view.filters import Filters, Cycler
_exports = ['body']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/layouts/content.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n\t<div class="row">\n\t\t<div class="col-md-8 col-md-offset-2">\n\t\t\t<img src="/static/images/logo-white.png" />\n\t\t\t<div class="panel panel-info">\n\t\t\t\t<div class="panel-heading">\n\t\t\t\t\t<div class="panel-title">\n\t\t\t\t\t\tPlease Login\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t<div class="panel-body">\n\t\t\t\t\t<form action="/login" method="post">\n\t\t\t\t\t\t<div class="form-group">\n\t\t\t\t\t\t\t<label for="username">Username</label>\n\t\t\t\t\t\t\t<input type="text" id="username" name="username" placeholder="Enter your Username" class="form-control"/>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t<div class="form-group">\n\t\t\t\t\t\t\t<label for="password">Password</label>\n\t\t\t\t\t\t\t<input type="password" id="password" name="password" placeholder="Enter your Password" class="form-control"/>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t<div class="form-group">\n\t\t\t\t\t\t<label for="keep_logged_in"><input type="checkbox" name="keep_logged_in" id="keep_logged_in" VALUE="Remember Me"/>&nbsp;Remember Me</label>\n\t\t\t\t\t\t\t<button type="submit" class="btn btn-info pull-right">Save</button>\n\t\t\t\t\t\t</div>\n\n\t\t\t\t\t</form>\t\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\t</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


