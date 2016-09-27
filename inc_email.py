import cgi
import os
import logging
from google.appengine.api import users, urlfetch
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.api import mail
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler

from time import time

from ath import gen

headers = {'User-Agent': "Lynx"}
f_email = str( gen('fwd_email') )

class ReceiveEmail(InboundMailHandler):
    def receive(self,message):
        sender = str( message.sender )
        recip  = str( message.to )
        subj   = str( message.subject )
        epoc   = str( time() )
        date   = str( message.date )
        logging.info( 'From: %s' % sender )
        logging.info( 'To: %s' % recip )
        try:
          logging.info('CC: %s' % message.cc)
        except:
          pass
        logging.info('Subject: %s' % subj )
        logging.info('Date: %s' % date )
        try:
          logging.info('Attachments: %s' % message.attachments) 
        except:
          pass
        plaintext = message.bodies(content_type='text/plain')
        for text in plaintext:
          txtmsg = ""
          txtmsg = text[1].decode()
          logging.info( 'Body is %s' % txtmsg )
          self.response.out.write( txtmsg )
          t = str( txtmsg )
          for url in t.split(' '):
             url = str( str( url ).split('\n')[0] )
             if '://' in url:
               lg = str( 'TRACE URL: %s' % url )
               logging.info(lg)       
               rsp = urlfetch.fetch(url, headers)
               sc  = str( rsp.status_code )
               logging.info( sc )

application = webapp.WSGIApplication([
  ReceiveEmail.mapping()
], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
