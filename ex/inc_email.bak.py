import cgi
import os
import logging
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.api import mail
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler

class ReceiveEmail(InboundMailHandler):
    def receive(self,message):
        logging.info("From: %s" % message.sender)
        logging.info("To: %s" % message.to)
        try:
          logging.info("CC: %s" % message.cc)
        except:
          pass
        logging.info("Subject: %s" % message.subject)
        logging.info("Date: %s" % message.date)
        try:
          logging.info("Attachments: %s" % message.attachments) 
        except:
          pass
        plaintext = message.bodies(content_type='text/plain')
        for text in plaintext:
            txtmsg = ""
            txtmsg = text[1].decode()
            logging.info("Body is %s" % txtmsg)
            self.response.out.write(txtmsg)

application = webapp.WSGIApplication([
  ReceiveEmail.mapping()
], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
