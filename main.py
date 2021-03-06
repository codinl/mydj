#!/usr/bin/env python
from django.core.wsgi import get_wsgi_application

from tornado.options import options, define
import config
import django.core.handlers.wsgi
import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi

os.environ['DJANGO_SETTINGS_MODULE'] = "settings"

define('port', type=int, default=config.server_port)


def main():
    wsgi_app = tornado.wsgi.WSGIContainer(django.core.wsgi.get_wsgi_application())
    tornado_app = tornado.web.Application([('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app))])
    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
