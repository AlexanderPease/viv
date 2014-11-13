import app.basic, settings, ui_methods
import logging
import tornado.web
from db.profiledb import Profile


########################
### Homepage
### /
########################
class Index(app.basic.BaseHandler):
  def get(self):
    return self.render('public/index.html')