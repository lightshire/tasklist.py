# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1388173225.521266
_enable_loop = True
_template_filename = u'/home/lightshire/todolist.py/application/views/shared/footer.html'
_template_uri = u'/shared/footer.html'
_source_encoding = 'utf-8'
from whirlwind.view.filters import Filters, Cycler
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n<div class="container footer">\n\t&copy; <script>document.write((new Date()).getFullYear());</script>. All rights reserved | Developed By: <a href="http://globalwebdynamics.net" target="_blank">Global Web Dynamics</a>\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


