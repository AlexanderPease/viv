import app.basic, settings, ui_methods
import logging
import tornado.web
from db.entrydb import Entry


########################
### Homepage
### /
########################
class Index(app.basic.BaseHandler):
  def get(self):
    return self.render('public/index.html')

class Submit(app.basic.BaseHandler):
  def post(self):
    logging.info('boo')

