# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1388187239.358511
_enable_loop = True
_template_filename = u'/home/lightshire/todolist.py/application/views/shared/flash_messages.html'
_template_uri = u'/shared/flash_messages.html'
_source_encoding = 'utf-8'
from whirlwind.view.filters import Filters, Cycler
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        flash = context.get('flash', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        if flash:
            # SOURCE LINE 4
            __M_writer(u'<div class="container">\n\t<div id="flash-message" class="flash-message">\n\t\t<div id="flash-message-list"></div>\n\t</div>\n</div>\n<script>\n\tvar message = "<div id=\'flash-message-items\' class=\'col-md-8 col-md-offset-2\'>";\n')
            # SOURCE LINE 11
            if 'error' in flash:
                # SOURCE LINE 12
                for message in flash['error']:
                    # SOURCE LINE 13
                    __M_writer(u'\t\t\tmessage += "<div class=\'alert alert-danger\'><span class=\'glyphicon glyphicon-exclamation-sign\'></span>&nbsp;')
                    __M_writer(filters.html_escape(unicode(message )))
                    __M_writer(u'</div>";\n')
            # SOURCE LINE 16
            if 'notice' in flash:
                # SOURCE LINE 17
                for message in flash['notice']:
                    # SOURCE LINE 18
                    __M_writer(u'\t\t\tmessage += "<div class=\'alert alert-warning\'><span class=\'glyphicon glyphicon-warning-sign\'></span>&nbsp;')
                    __M_writer(filters.html_escape(unicode(message )))
                    __M_writer(u'</div>";\n')
            # SOURCE LINE 21
            if 'info' in flash:
                # SOURCE LINE 22
                for message in flash['info']:
                    # SOURCE LINE 23
                    __M_writer(u'\t\t\tmessage += "<div class=\'alert alert-info\'><span class=\'glyphicon glyphicon-comment\'></span>&nbsp;')
                    __M_writer(filters.html_escape(unicode(message )))
                    __M_writer(u'</div>";\n')
            # SOURCE LINE 26
            if 'success' in flash:
                # SOURCE LINE 27
                for message in flash['success']:
                    # SOURCE LINE 28
                    __M_writer(u'\t\t\tmessage += "<div class=\'alert alert-success\'><span class=\'glyphicon glyphicon-ok\'></span>&nbsp;')
                    __M_writer(filters.html_escape(unicode(message )))
                    __M_writer(u'</div>";\n')
            # SOURCE LINE 31
            __M_writer(u'\tmessage += "</div>";\n\tshowNotification(message, \'\', function(){});\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


