import app.basic, settings, ui_methods
import logging, datetime
import tornado.web
from db.entrydb import Entry


########################
### AddEntry
### User clicked "Learn More"
### api/addentry
########################
class AddEntry(app.basic.BaseHandler):
  def post(self):
    logging.info("POST to /addentry")
    session_id = self.get_argument('session_id','')
    age = self.get_argument('age','')
    gender = self.get_argument('gender','')
    kids = self.get_argument('kids','')
    income = self.get_argument('income','')
    mortgage = self.get_argument('mortgage','')
    height = self.get_argument('height','')
    weight = self.get_argument('weight','')
    coverage_amount = self.get_argument('coverage_amount','')
    coverage_term = self.get_argument('coverage_term','')

    if session_id:
      try:
        entry = Entry.objects.get(session_id=session_id)
        logging.info("Entry alread exists for session_id: %s" % session_id)
      except:
        entry = None

      # If entry already exists, it's the same user clicking again. Ignore.
      if not entry:
        try:
          entry = Entry(date=datetime.datetime.now(),
            session_id=session_id,
            age=age,
            gender=gender,
            kids=kids,
            income=income,
            mortgage=mortgage,
            height=height,
            weight=weight,
            coverage_amount=coverage_amount,
            coverage_term=coverage_term
          )
          entry.save()
          logging.info()
        except:
          logging.warning('Could not create entry:')
          logging.warning('Age: %s' % age)
          logging.warning('Gender: %s' % gender)
          logging.warning('Kids: %s' % kids)
          logging.warning('Income: %s' % income)
          logging.warning('Mortgage: %s' % mortgage)
          logging.warning('Height: %s' % height)
          logging.warning('Weight: %s' % weight)
          logging.warning('Coverage Amount: %s' % coverage_amount)
          logging.warning('Coverage Term: %s' % coverage_term)
    return

########################
### ModalEntry
### User submitted name and email from the modal
### api/modalentry
########################
class ModalEntry(app.basic.BaseHandler):
  def post(self):
    logging.info("POST to /modalentry")
    session_id = self.get_argument('session_id','')
    name = self.get_argument('name','')
    email = self.get_argument('email','')

    try:
      entry = Entry.objects.get(session_id=session_id)
    except:
      logging.info("Could not find Entry of session_id %s" % session_id)
      logging.warning('Name: %s' % name)
      logging.warning('Email: %s' % email)
      return

    if entry:
      try:
        entry.name = name
      except:
        logging.warning('Could not add name')
      entry.email = email
    return