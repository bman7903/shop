#!/usr/bin/env python

#mongo     = 'thingsnstuff'
musr_name  = 'stuffnthings'
musr_pwd   = 'GofuckyourselF1'
uniq_db    = 'ds061454'
db_port    = '61454'
ml_db      = 'tmpusr'
ml_tcl     = 'tmp'
mapi_key   = '7Yf-GxfLIVK4urGDSQ9Aa9V4EOe-7XAy'
key_db     = 'keydb'
bad_db     = 'baddb'
kart_db    = 'k4rt'
m_blaster  = 'masterdb'

## General
fw_email    = 'bman7903@gmail.com'

## DNS
f_usr       = 'freedns@things-n-stuff.appspotmail.com'
f_pswd      = 'GofuckyourselF'

### Mandril L1 API < ( FWD NX PTR cloud 2 app )
aapi_key = 'UsNLXKHBZBwYDUeClRw3gw'

#http://[USERNAME]:[PASSWORD]@freedns.afraid.org/nic/update?hostname=[DOMAIN]&myip=[IP]
#(https/SSL is also optionally supported/available)


def gen( proc ):
  def fwd_email():
     return fw_email
  t = eval( proc )
  return t()

def flux( proc ):
  def usr():
     return f_usr
  def pswd():
     return f_pswd
  def crdz():
     f = str( usr() )
     p = str( pswd() )
     c = str( '[%s]:[%s]' % (f,p) )
     return c
  def uri():
     c   = str( crdz() )
     u   = str('https://%s@freedns.afraid.org/nic/update?hostname=[DOMAIN]&myurl=[IP]' % c )
     return u
  t = eval( proc )
  return t()

def mlab( proc ):
  def usr():
     return musr_name
  def pswd():
     return musr_pwd
  def m_db():
     return ml_db
  def tml_cl():
     return ml_tcl
  def muniq():
     return uniq_db
  def mport():
     return db_port
  def mkey():
     return mapi_key
  def keydb():
     return key_db
  def masta():
     return m_blaster
  def baddb():
     return bad_db
  def k_db():
     return kart_db
  t = eval( proc )
  return t()

def mdrill( proc ):
  def akey():
     return aapi_key
  t = eval( proc )
  return t
