import app.basic, ui_methods
import tornado.web
import settings
import requests, datetime, logging
from db.entrydb import Entry



###########################
### List the available admin tools
### /admin
###########################
class AdminHome(app.basic.BaseHandler):
    #@tornado.web.authenticated
    def get(self):
        return self.render('admin/admin_home.html')


###########################
### ASCII view of database
### /admin/db_entry
###########################
class DB_Entry(app.basic.BaseHandler):
    #@tornado.web.authenticated
    def get(self):
        entries = Entry.objects
        return self.render('admin/db_entry.html', entries=entries)