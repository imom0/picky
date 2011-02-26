#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import urllib

from v2ex.picky.security import CheckAuth, DoAuth
from v2ex.picky.ext.sessions import Session

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.ext.webapp.util import run_wsgi_app

class File(db.Model):
    name = db.StringProperty()
    property = db.StringProperty()
    bits = db.BlobProperty(default=None)
    date = db.DateTimeProperty(auto_now_add=True)


class Pic(webapp.RequestHandler):
    def get(self,slug):
        if slug:
            name = unicode(urllib.unquote(slug),'utf8')
            q_file = db.GqlQuery("SELECT * FROM File WHERE name = :1",name)
            if q_file.count() == 1:
                q_file = q_file[0]
                self.response.headers['Content-Type'] = str(q_file.property)
                self.response.headers['Cache-Control'] = "max-age=172800, public, must-revalidate"
                self.response.headers['Expires'] = "Thu, 20 Dec 2012 20:00:00 GMT"
                self.response.out.write(q_file.bits)
            else:
                self.redirect('/file/')
        else:
            path = os.path.join(os.path.dirname(__file__),'tpl','themes','default','file.html')
            values = ""
            output = template.render(path,values)
            self.response.out.write(output)
        
    def post(self,slug):
        self.session = Session()
        if CheckAuth(self) is False:
            return DoAuth(self, '/writer/overview')
        name = self.request.get('filename')
        mtype = self.request.get('fileext')
        bits = self.request.get('upfile')
        new_file = File(name=name,property=mtype,bits=bits)
        new_file.put()
        self.response.out.write("![%s](/file/%s)" % (name,urllib.quote(name.encode('utf8'))))


app = webapp.WSGIApplication([('/file/([^/]*)/{0,1}.*',Pic)],debug=True)

if __name__ == "__main__":
    run_wsgi_app(app)
