# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1388332194.826149
_enable_loop = True
_template_filename = u'/home/lightshire/todolist.py/application/views/layouts/base.html'
_template_uri = u'/layouts/base.html'
_source_encoding = 'utf-8'
from whirlwind.view.filters import Filters, Cycler
_exports = ['scripts', 'page_title', 'head_tags']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'<!doctype html>\n<!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="en"> <![endif]-->\n<!--[if IE 7]>    <html class="no-js lt-ie9 lt-ie8" lang="en"> <![endif]-->\n<!--[if IE 8]>    <html class="no-js lt-ie9" lang="en"> <![endif]-->\n<!--[if gt IE 8]><!-->\n<html class="no-js" lang="en">\n<!--<![endif]-->\n<head>\n\t\n\t')
        # SOURCE LINE 11
        __M_writer(u'\n\t<title>\n\t\t')
        # SOURCE LINE 13
        __M_writer(unicode(self.page_title()))
        __M_writer(u'\n\t</title>\n\t\n\t<meta charset="utf-8">\n\t<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">\n\t<meta name="keywords" content="" />\n\t<meta name="description" content="">\n\t<meta name="viewport" content="width=device-width">\n\t<link rel="shortcut icon" href="/static/images/logo-square.png" />\n\t<link rel="stylesheet" href="/static/css/bootstrap.css?')
        # SOURCE LINE 22
        __M_writer(unicode(Filters.version()))
        __M_writer(u'">\n\t\n\t<link rel="stylesheet" href="/static/css/style.css?')
        # SOURCE LINE 24
        __M_writer(unicode(Filters.version()))
        __M_writer(u'" />\n\t<!--[if lt IE 9]>\n\t\t<script src="http://html5shim.googlecode.com/svn/trunk/html5-els.js"></script>\n\t<![endif]-->\n\n\t<script src="//ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>\n\n\t<script src="/static/js/whirlwind.js?')
        # SOURCE LINE 31
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\n\t<script src="/static/js/application.js?')
        # SOURCE LINE 32
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\n\t<script src="/static/js/flash-messages.js?')
        # SOURCE LINE 33
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\n\t')
        # SOURCE LINE 34
        __M_writer(unicode(self.head_tags()))
        __M_writer(u'\n\t')
        # SOURCE LINE 35
        __M_writer(u'\n</head>\n<body>\n\t<!--[if lt IE 7]><p class=chromeframe>Your browser is <em>ancient!</em> <a href="http://browsehappy.com/">Upgrade to a different browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">install Google Chrome Frame</a> to experience this site.</p><![endif]-->\n\t')
        # SOURCE LINE 39
        __M_writer(unicode(next.body()))
        __M_writer(u'\n\t')
        # SOURCE LINE 40
        __M_writer(unicode(self.scripts()))
        __M_writer(u' \n\t')
        # SOURCE LINE 41
        __M_writer(u'\n\t<script type="text/javascript" src="/static/js/jquery.js"></script>\n\t<script>window.jQuery || document.write(\'<script src="/static/js/jquery-1.7.1.min.js"><\\/script>\')</script>\n\t<script type="text/javascript" src="/static/js/bootstrap.js?')
        # SOURCE LINE 44
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\n\t<script type="text/javascript" src="/static/js/backstretch.js?')
        # SOURCE LINE 45
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\n\t<script type="text/javascript">\n\t\t$(document).ready(function() {\n\t\t\t$.backstretch("/static/images/background.jpg");\n\t\t});\n\t</script>\n\t<script>\n\t\tvar _gaq=[[\'_setAccount\',\'UA-XXXXX-X\'],[\'_trackPageview\']];\n\t\t(function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];\n\t\tg.src=(\'https:\'==location.protocol?\'//ssl\':\'//www\')+\'.google-analytics.com/ga.js\';\n\t\ts.parentNode.insertBefore(g,s)}(document,\'script\'));\n\t</script>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_scripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 11
        __M_writer(u'TodoList.Py')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_tags(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


