from google.appengine.api.logservice import logservice
from google.appengine.api import users, urlfetch #, modules
#from google.appengine.ext import testbed
from base64 import urlsafe_b64decode
from random import choice, getrandbits
from time import time
from re import sub
from os import environ

import webapp2, cgi
import requests, json, hashlib
import logging

from webc import mainpage, signup, confirm, terms, portal, infro, HEAD, TAIL, myhome, preadd, preerr, monkey, lots
from mand import smail
from mong import pst, req, u2s, s2u, s2t, luzr, idc, lstc, deld, retc
from wall import wall
from kart import addto
from ath import mlab
from ldb import rselect

mongolab_key = str( mlab('mkey') )
tusr_db      = str( mlab('m_db') )
tusr_cl      = str( mlab('tml_cl') )
utmpdb       = str( 'databases/' + tusr_db + ' /collections/' + tusr_cl )
keydb        = str( mlab('keydb') )
baddb        = str( mlab('baddb') )
mstr         = str( mlab('masta') )

femail       = 'Chuck-Norris@chuck.norris'
fname        = 'Chuck-Norris'


def rpic( dir, query, n ):
  query  = str( query )
  idir   = 'img'
  q      = []
  bdir   = str( idir + '/' + str( dir ) )
  for x in range(1, n):
     img = str( bdir + '/' + query + str(x) + '.png' )
     q.append( img )
  ic  = str(  choice(q) )
  return ic

def CONFIRM( User ):
  User = str( User )
  conf =  '''\
     <div id="content-wrapper"><div id="content">
       <br><br><label><b>
       <form action="/welcome" method="post"><pre>
       <label>  Thank you for joining!</b></label><br>
       <br><br>  You will recieve a email with a confirmation number shortly<br>
       <br> please copy the confirmation string into the box belong and click submit.<br>
       <img src="img/oneofus.png">
       <br> Username: <input type="text" name="User" value="'''+User+'''" style="width: 100px; height: 25px;"> Conf-String:
       <input type="text" name="confstring" style="width: 200px; height: 25px;">&nbsp <input type="submit" value="Submit"></form>
    </div></div> '''
  return conf

HEADU = """\
  <html> <head> Loading...
  <link rel="stylesheet" type="text/css" href="css/box.css" />
  <!--For versions below Internet Explorer 7-->
  <!--[if lt IE 7]>
  <link rel="stylesheet" href="css/unreal.css" type="text/css">
  <![endif]-->
  <style>.standard_label_style { color: yellow; }</style>
  </head>
  <body background="img/greent.png">
     <div id="content-wrapper"><div id="content">
       <br><br> """

def userland( userinfo, fstrn ):
  userinfo = str( userinfo )
  fstrn    = str( fstrn )
  landing  = """ \
  <div id="content-wrapper"><div id="content"><br><br><b>
     <div><b>  <label>Welcome!<pre><label><br></b>
     <div>        you how now logged in with your info """ + userinfo + """ \
     <div>        matched string """ + fstrn  + """ </div>
     </div><div>                <img src="img/fairy.png"></pre></div>
  </div></div> """
  return landing

def badcred( userinfo, fstrn ):
  userinfo = str( userinfo )
  fstrn    = str( fstrn )
  landing = """ \
  <div id="content-wrapper"><div id="content"><br><br><b>
     <div><b>  <label>Shucks!!!<pre><label><br></b>
     <div>        there is some thing funny about that string</div> """ + userinfo + """ \
     <div>        was looking for """ + fstrn +  """ </div> 
     <div>                <img src="img/fairy.png"></pre></div>
  </div></div> """
  return landing

def dberror():
  landing = """ \
  <div id="content-wrapper"><div id="content"><br><br><b>
     <div><b>  <label>Shucks!!!<pre><label><br></b></div>
     <div>        Trouble with server, try later</div>
     <div>                <img src="img/fairy.png"></pre></div>
  </div></div> """
  return landing

def fuck():
  f = "<html><body><br><br><div> ... What the fuck what that!? </div></br></br></body></html>"
  return f

def Headers( headers, proc ):
  g    = str( headers )
  proc = str( proc )
  logging.info( g )
  def all():
     h = []
     for e in str( headers ).split('\n'):
       e = str( e )
       h.append(e)
     return h
  def item():
     for e in str( headers ).split('\n'):
       e = str( e )
       if '-' in e:
          if '_' in e:
            itm = str( e.split('=')[0] )
            id  = str( itm.split('_')[-1] )
            if len( id ) == 25:
               if id[0].isdigit():
                 return itm
  t = eval( proc )
  return t()

def uprc( rc ):
  c = str( rc )
  for i in rc.split(','):
     i = str( str( i ).strip() )
     j = str( i.split(':')[0] )
     k = str( i.split(':')[-1] )
     k = str( sub('"','', k ) )
     k = str( k.strip() )
     if 'full_name' in j:
       LName  = k
     if 'email' in j:
       Email  = k
     if 'password' in j:
       Scrt   = k
     if 'question' in j:
       sQues  = k
     if 'sanswer' in j:
       sAnsw  = k
     if 'social' in j:
       Social = k
     if 'news' in j:
       News   = k
  return Scrt, LName, Email, Social

def checkCstrn( fstrn, mongolab_key, rc ):
  fstrn = str( fstrn )
  for k in rc.split('{ "_id"'):
     k = str( k )
     if fstrn in k:
        landing = userland( k, fstrn )
        return landing

def shaStr( o ):
  m = hashlib.sha1()
  m.update( o )
  o = str(m.hexdigest())
  return o 

def MYHOME( User, pswd ):
#  ustr   = str( cgi.escape(self.request.get('uzer')) )
  User   = str( User )
  ustr   = str( u2s( User ) )
  url    = str( "https://api.mongolab.com/api/1/databases/" + tusr_db + "/collections/" + User + "?apiKey=" + mongolab_key )
  result = urlfetch.fetch(url)
  if result.status_code == 200:
     rc     = result.content
     usrc   = uprc( rc )
     Scrt   = usrc[0]
     lname  = usrc[1]
     Email  = usrc[2]
     try:
       Social = usrc[3]
     except:
       pass

     lots = luzr( User )

     try:
       if ustr == pswd:
          landing  = str( myhome( User, ustr, lots, 'landing' ) )
          return landing
     except:
       pass


     if str( shaStr( pswd ) )  == str( Scrt ):
          landing  = str( myhome( User, ustr, lots, 'landing' ) )
     else:       landing  = """ \
          <div id="content-wrapper"><div id="content"><br><br><b>
            <div><b>  <label> Your Failed Dude! <pre><br></b>
            <div>        Bad password. try again. </div></label>
            <div>        expected """ + str( shaStr( Scrt ) ) + """ got """ + pswd + """ </div>
            </div><div>                <img src="img/fairy.png"></pre></div>
          </div></div> """
     return landing

  else:
     sc = str( result.status_code )
     er = str( 'Bad request, %s %s' % (sc + url) )
     logging.info( er )
     rc = str( result.content )
     for e in rc.split('\n'):
       e = str( e )
       logging.info( e )
     fk = str( fuck() )
     return fk

class MainPage(webapp2.RequestHandler):
     def do(self, proc):
        proc = str( proc )
        r = requests.get('http://freedns.afraid.org/dynamic/update.php?MVk5YWZWVUFKUFZablpiVnptaTVNekp2OjE1NjI2NTg3')
        rsp = str( r.status_code )
        cnt = str( r.content )
        logging.info('trying to update dns' )
        li = str( '%s: %s' % ( rsp, cnt ) )
        logging.info( li )
        try:
          offset = self.request.get('offset') or None
          if offset:
             offset = urlsafe_b64decode(str(offset))
        except:
          offset    = None
        end_time    = time()
        count       = 5
        show_next   = False
        last_offset = None
        i           = 1
        for req_log in logservice.fetch(end_time=end_time, offset=offset, 
        minimum_log_level=logservice.LOG_LEVEL_INFO, include_app_logs=True):
          ip   = str( req_log.ip )
          rq = str( req_log )
          if proc == 'post':
             try:
                 iid  = str( environ['INSTANCE_ID'] )
                 li   = str( '[+] INTANCE: ' + iid )
                 logging.info( li )
                 mfy  = str( cgi.escape(self.request.params.get('kart')) )
                 addto( ip, mfy, iid ) 
             except:
                 logging.info( '[-] unable to add item' )
          meth = str( req_log.method )
          rec  = str( req_log.resource )
          q    = str( wall( baddb, 'check', ip ) )
          if q == 'True':
             img  = str( rpic( 'monkey', 'badmonkey', 8 ) )
             HTML = str( monkey( 'bad', img ) )
             li   = str( '[-] BAD IP: ' + ip + '  -METHOD: ' + meth + '  -RESOURCE:' + rec  )
             logging.info( li )
             self.response.write(HTML)
             return
          li   = str( 'IP: ' + ip + '  -METHOD: ' + meth + '  -RESOURCE:' + rec ) # + '\n -INSTANCE:' + ins )
          logging.info( li )
          break
        for e in environ:
          e = str( e )
          t = str( environ[e] )
          q = str( e + ': ' + t )
          logging.info( q )
        imgz = str( rselect( mstr ) )
        HTML = str( mainpage( imgz ) )
        self.response.write(HTML)
     def post( self ):
        self.do('post')
     def get( self ):
        self.do('get')


class signupPage(webapp2.RequestHandler):
    def get(self):
        HTML = str( signup() )
        self.response.write(HTML)

class MyAdd(webapp2.RequestHandler):
  def do( self ):
     g = self.request
     h = Headers( g, 'all' )
     ustr   = str( cgi.escape(self.request.get('uzer')) )
     try:
       mfy  = str( cgi.escape(self.request.params.get('modify')) )
     except:
       mfy  = 'None'
     User   = str( s2u( ustr ) )

     i    = idc( User, 'item', mfy )
     mfy  = lstc( User, i )
     HTML = str( myhome( User, ustr, mfy, 'edit' ) )

     for e in h:
       e = str( e )
       if 'delete=Del' in e:
          doc = str( e.split('=')[-1] )
          id  = idc( User, 'item', doc )
          deld( User, id )
          HTML = str( MYHOME( User, ustr ) )
     if mfy  == 'None':
       HTML = str( myhome( User, ustr, mfy, 'add' ) )
     self.response.write(HTML)
  def post( self ):
     self.do()
  def get( self ):
     self.do()

class MyDel(webapp2.RequestHandler):
  def do( self, proc ):
     proc = str( proc )
     if proc == 'post':
#       g = self.request
#       Headers( g )
       ustr   = str( cgi.escape(self.request.get('uzer')) )
       try:
          mfy  = str( cgi.escape(self.request.params.get('modify')) )
       except:
          mfy  = 'None'
       User   = str( s2u( ustr ) )
       HTML = str( myhome( User, ustr, mfy, 'remove' ) )
       self.response.write(HTML)
  def post( self ):
     self.do('post')
  def get( self ):
     self.do('get')

class MyCopy(webapp2.RequestHandler):
  def do( self, proc ):
     proc = str( proc )
     if proc == 'post':
       HTML = str( myhome( 'copy' ) )
       self.response.write(HTML)
  def post( self ):
     self.do('post')
  def get( self ):
     self.do('get')

class TOS(webapp2.RequestHandler):
  def get( do, proc ):
    proc = str( proc )
    if proc == 'get':
       HTML = str( terms( 'TOS' ) )
       self.response.write(HTML)
  def post( self ):
     self.do('post')
  def get( self ):
     self.do('get')

class Lot(webapp2.RequestHandler):
  def do( self, proc ):
     proc = str( proc )
     g = self.request
     itm = Headers( g, 'all' )
     li  = str( 'ITEM ' + str( itm ) )
     logging.info( li )
#     dky = str( Headers( g, 'item' ) )
     dky  = str( cgi.escape(self.request.get('oid')) )
     li   = str( '-CKY:  ' + dky )
     logging.info( li )
     oid  = str( dky.split('_')[0] )
     t    = str( dky.split('_')[-1] )
     User = str( t.split('-')[0] )
     item = str( t.split('-')[-1] )
     oid  = str( idc( User, 'item', item ) )
     ouid = oid
     rc   = str( retc( User, oid ) )
     logging.info( rc )
     for e in rc.split(', '):
          e  = str( e )
          h  = str( e.split(' : ')[0] )
          g  = str( e.split(' : ')[-1] )
          lg = ( len( g ) - 2 )
          if 'oid' in h:
            oid    = g
          if 'item' in h:
            item   = str( g[1:lg] )
          if 'subc' in h: 
            subc = str( g[1:lg] )
          if 'gory' in h:
            gory   = str( g[1:lg] )
          if 'price' in h:
            price  = g
          if 'img3' in h:
            img3   = str( g.strip() )
          if 'img2' in h:
            img2   = str( g.strip() )
          if 'ship' in h:
            ship   = g
          if 'img1' in h:
            img1   = str( g.strip() )
          if 'desc' in h:
            desc   = g
          if 'lts' in h:
            lts    = g
          if 'pcs' in h:
            pcs    = g
          if 'info' in h:
            info   = g
          if 'ouid' in h:
            ouid   = g
     HTML = str( lots( oid, User, item, gory, subc, desc, img1, img2, img3, price, ship, lts, pcs, info, ouid ) )
     self.response.write( HTML )
  def post( self ):
     self.do('post')
  def get( self ):
     self.do('get')

class PreAdd(webapp2.RequestHandler):
  def do( self, proc ):
     proc = str( proc )
     if proc == 'post':
#       g = self.request
#       Headers( g )
       ustr   = str( cgi.escape(self.request.get('uzer')) )
#       User   = str( s2u( ustr ) )
       item   = str( cgi.escape(self.request.get('item')) )
       gory   = str( cgi.escape(self.request.get('cat')) )
       subcat = str( cgi.escape(self.request.get('sub-cat')) )
       desc   = str( cgi.escape(self.request.get('desc')) )
       price  = int( cgi.escape(self.request.get('price')) )
       ship   = int( cgi.escape(self.request.get('shipping')) )
       img1   = str( cgi.escape(self.request.get('image1')) )
       img2   = str( cgi.escape(self.request.get('image2')) )     
       img3   = str( cgi.escape(self.request.get('image3')) )
       pcs    = int( cgi.escape(self.request.get('pieces')) )
       lts    = int( cgi.escape(self.request.get('lots')) )
       info   = str( cgi.escape(self.request.get('more')) )
       reqs   = [ 'item','gory','desc','price','ship','img1','pcs' ]
       items  = [ 'item','gory','subcat','desc','price','ship','img1','img2','img3','pcs','lts','info','User' ]
       stuff  = []
       ers    = []
       for e in reqs:
          d = str( e )
          e = eval( e )
          e = str( e )
          if len( e ) < 1:
            er = str( '%s is mandatory' % d )
            ers.append( er )
       if not '://' in img1:
          er = str( 'URL must be complete, IE "http://www.example.com/favicon.ico"' )
          ers.append( er )
       if len( img2 ) > 0:
          if not '://' in img2:
            er = str( 'URL must be complete, IE "http://www.example.com/favicon.ico"' )
            ers.append( er )
       if len( img3 ) > 0:
          if not '://' in img3:
            er = str( 'URL must be complete, IE "http://www.example.com/favicon.ico"' )
            ers.append( er )
       if not isinstance( price, int ):
          er = str( 'Price is USD with NO CHANGE' )
          ers.append( er )
       if not isinstance( pcs, int ):
          er = str( 'Integer Required for Pieces Per Lot' )
          ers.append( er )
       s = str( ship )
       t = str( lts )
       if len( t ) > 0:
          if not isinstance( lts, int ):
            er = str( 'Ineger Required for Total Lots' )
            ers.append( er )
       if len( s ) > 0:
          if not isinstance( ship, int ):
            er = str( 'Shipping is USD with no CHANGE' )
            ers.append( er )

       if len( ers ) > 1:
          HTML   = str( preerr( ers ) )
          self.response.write(HTML)
          return
          
       User   = str( s2u( ustr ) )
       Data = [
             {
               'item':item,
               'gory':gory,
               'subcat':subcat,
               'desc':desc,
               'price':price,
               'ship':ship,
               'img1':img1,
               'img2':img2,
               'img3':img3,
               'pcs':pcs,
               'lts':lts,
               'info':info,
               'User':User,
             }
            ]

       pst( User, Data )
       ouid = str( idc( User, 'item', item ) )
       Data2 = [
             {
               'item':item,
               'gory':gory,
               'subcat':subcat,
               'desc':desc,
               'price':price,
               'ship':ship,
               'img1':img1,
               'img2':img2,
               'img3':img3,
               'pcs':pcs,
               'lts':lts,
               'info':info,
               'User':User,
               'ouid':ouid,
             }
            ]
       pst( mstr, Data2 )
       for e in items:
          e = eval( e )
          stuff.append( e )         
       HTML   = str( preadd( ustr, stuff ) )
       self.response.write(HTML)

  def post( self ):
     self.do('post')
  def get( self ):
     self.do('get')

class INFO(webapp2.RequestHandler):
  def do( self ):
     HTML = str( infro('INFO') )
     self.response.write(HTML)
  def post( self ):
     self.do()
  def get( self ):
     self.do()

class PORTAL(webapp2.RequestHandler):
  def do( self, proc ):
     proc = str( proc )
     if proc == 'get':
        try:
          offset = self.request.get('offset') or None
          if offset:
             offset = urlsafe_b64decode(str(offset))
        except:
          offset    = None
        end_time    = time()
        count       = 5
        show_next   = False
        last_offset = None
        i           = 1
        for req_log in logservice.fetch(end_time=end_time, offset=offset, minimum_log_level=logservice.LOG_LEVEL_INFO, include_app_logs=True):
          ip   = str( req_log.ip )
          meth = str( req_log.method )
          rec  = str( req_log.resource )
          q    = str( wall( baddb, 'check', ip ) )
          if q == 'True':
             img  = str( rpic( 'monkey', 'badmonkey', 8 ) )
             HTML = str( monkey( 'bad', img ) )
             li   = str( '[-] BAD IP: ' + ip + '  -METHOD: ' + meth + '  -RESOURCE:' + rec  )
             logging.info( li )
             self.response.write(HTML)
             return
          li   = str( 'IP: ' + ip + '  -METHOD: ' + meth + '  -RESOURCE:' + rec  )
          logging.info( li )
          break
        HTML    = str( portal('LOGIN') )
        self.response.write(HTML)
  def post( self ):
     self.do( 'post' )
  def get( self ):
     self.do( 'get' )

class MyHome(webapp2.RequestHandler):
  def do( self, act ):
     act      = str( act )
#     g = self.request
#     Headers( g )
     try:
       offset = self.request.get('offset') or None
       if offset:
          offset = urlsafe_b64decode(str(offset))
     except:
       offset    = None
     end_time    = time()
     count       = 5
     show_next   = False
     last_offset = None 
     i           = 1
     for req_log in logservice.fetch(end_time=end_time, offset=offset, minimum_log_level=logservice.LOG_LEVEL_INFO, include_app_logs=True):
       ip   = str( req_log.ip )
       meth = str( req_log.method )
       rec  = str( req_log.resource )
       q    = str( wall( baddb, 'check', ip ) )
       if q == 'True':
          img  = str( rpic( 'monkey', 'badmonkey', 8 ) )
          uHome = str( monkey('bad', img) )
          li   = str( '[-] BAD IP: ' + ip + '  -METHOD: ' + meth + '  -RESOURCE:' + rec  )
          logging.info( li )
          self.response.write(uHome)
          return 
       break
     if act == 'post':  
        pswd  = str( cgi.escape(self.request.get('passwd')) )
        User  = str( cgi.escape(self.request.get('user')) )
        ustr = str( cgi.escape(self.request.get('uzer')) )
        if len( ustr ) > 6:
          User = str( s2u( ustr ) )
          uHome = str( MYHOME( User, ustr ) )
        else:
          uHome = str( MYHOME( User, pswd ) )
          er = str( 'User %s' % User )
          logging.info( er )
          er = str( 'ustr %s ' %ustr )
          logging.info( er )
        li   = str( 'IP: ' + ip + '  -METHOD: ' + meth + '  -RESOURCE:' + rec  )
        logging.info( li )
#        self.response.write(uHome)
     if act == 'get':
        li   = str( '[-] BAD METHOD IP: ' + ip + '  -METHOD: ' + meth + '  -RESOURCE:' + rec  )
        logging.error( li )
        img  = str( rpic( 'monkey', 'badmonkey', 8 ) )
        uHome = str( monkey('bad', img) )
     self.response.write(uHome)
  def post( self ):
     self.do( 'post' )
  def get( self ):
     self.do( 'get' )

class WELCOME(webapp2.RequestHandler):
  def do( self ):
     fstrn  = str( cgi.escape(self.request.get('confstring')) )
     User   = str( cgi.escape(self.request.get('User')) )
     url = str( "https://api.mongolab.com/api/1/databases/" + tusr_db + "/collections/" + User + "?q={}&apiKey=" + mongolab_key )
     lg = str( 'Fetching URL %s' % url )
     logging.info( lg )
     result = urlfetch.fetch(url)
     sc = result.status_code
     if sc == 200:
       rc     = result.content
       MID    = str( checkCstrn( fstrn, mongolab_key, rc )  )
       HTML   = str( str( HEAD() ) + MID + str( TAIL("You don't look framilier...") ) )
       self.response.write(HTML)
       if 'Welcome!' in MID:
          c = str( rc )
          for i in rc.split(','):
            i = str( str( i ).strip() )
            j = str( i.split(':')[0] )
            k = str( i.split(':')[-1] )
            k = str( sub('"','', k ) )
            k = str( k.strip() )
            if 'full_name' in j:
               LName  = k
            if 'email' in j:
               Email  = k
            if 'password' in j:
               Scrt   = k
            if 'question' in j:
               sQues  = k
            if 'sanswer' in j:
               sAnsw  = k
            if 'social' in j:
               Social = k
            if 'news' in j:
               News   = k
            if 'user_name' in j:
               User   = k
            Active = 'True'
                   
          DATA = [
                            {
                               'full_name': LName,
                               'user_name': User,
                               'email': Email,
                               'password': Scrt,
                               'social': Social,
                               'news': News,
                               'question': sQues,
                               'sanswer': sAnsw,
                               'active':Active,
                            }
                          ]

          api        = {"q":"{}","apiKey": mongolab_key}
          http_start = "https://api.mongolab.com/api/1/"
          http_type  = str( "databases/" +  tusr_db + "/collections/" + User )
          headers    =   {"Content-Type": "application/json"} 
          r = requests.put(http_start+http_type, params=api, headers=headers,data = json.dumps(DATA))
          sc = r.status_code
          rc = r.content
          if sc == 200:
              MID  = str( DATA  )
              HTML   = str( str( HEAD() ) + MID + str( TAIL("You don't look framilier") ) )      
          er = str( 'Uknown error, ' + str( sc ) + ' check config \n\n' + rc )
          logging.info( er )
     else:
       logging.info( sc )

  def post( self ):
     self.do()
  def get( self ):
     self.do()

class confirmPage(webapp2.RequestHandler):
  def badForm( self ):
     self.response.write('<html><body>A Required Form is Empty!<pre>')
     self.response.write('\n')
     self.response.write('fix it...')
     self.response.write('</pre></body></html>')
     return

  def do(self): 
     fName  = str( cgi.escape(self.request.get('fname')) )
     lName  = str( cgi.escape(self.request.get('lname')) )
     LName  = str( fName + ' ' + lName )
     User   = str( cgi.escape(self.request.get('user')) )
     Email  = str( cgi.escape(self.request.get('email')) )
     passa  = str( cgi.escape(self.request.get('passwda')) )
     passb  = str( cgi.escape(self.request.get('passwdb')) )
     Social = str( cgi.escape(self.request.get('social_x')) )
     News   = str( cgi.escape(self.request.get('news_x')) )
     sQues  = str( cgi.escape(self.request.get('squestion')) )
     sAnsw  = str( cgi.escape(self.request.get('sanswer')) )
     lp     = len( passa )

     if not passa == passb:
       self.response.write('<html><body>Passwords Dont Match!<pre>')
       self.response.write('\n')
       self.response.write('Would you like to play again?')
       self.response.write('</pre></body></html>')
       return

     if lp < 10:
       self.response.write('<html><body>Ten Digit Password Required<pre>')
       self.response.write('\n')
       self.response.write('Would you like to play again?')
       self.response.write('</pre></body></html>')
       return

     for e in 'fName lName Email sQues sAnsw'.split(' '):
       k  = eval( e )
       l  = len( k )
       if l < 1:
          self.badForm()
          return

     pswd = str( shaStr( passa ) )
     o = str( LName + User + pswd )
     o = str( shaStr( o ) )
     rnd = str( getrandbits(128) )
     tme = str( str( time() ).split('.')[0] )

     DATA = [
           {
           'full_name': LName,
           'user_name': User,
           'email': Email,
           'password': pswd,
           'social': Social,
           'news': News,
           'question': sQues,
           'sanswer': sAnsw,
           'confstrn': o

           }
        ]

     DATA2 = [ 
            {
            'user_name': User,
            'password': pswd,
            'usrstrn': rnd,
            'time': tme
             }
        ]

     api = {"apiKey": mongolab_key}
     http_start = "https://api.mongolab.com/api/1/"
     http_type  = str( "databases/" + tusr_db + "/collections/" + User )
     http_t     = str( "databases/" + tusr_db + "/collections/" + keydb )
     headers    = {"Content-Type": "application/json"}

     r = requests.post(http_start+http_type, params=api, headers=headers,data = json.dumps(DATA))
     smail( Email, 'Confirmation Required', o, User, femail, fname )
     r = requests.post(http_start+http_t, params=api, headers=headers,data = json.dumps(DATA2) )
     cnf = str( CONFIRM( User ) )
     HTML = str(  confirm( cnf )  )
     self.response.write(HTML)
 
  def post( self ):
     self.do()
  def get( self ):
     self.do()

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/signup', signupPage),
    ('/confirm', confirmPage),
    ('/tos', TOS),
    ('/login', PORTAL),
    ('/info', INFO),
    ('/welcome', WELCOME),
    ('/my-home', MyHome),
    ('/home-add', MyAdd),
    ('/pre-add', PreAdd),
    ('/home-del', MyDel),
    ('/home-copy', MyCopy),
    ('/lot', Lot),
#    ('/check-out', CheckOut),
], debug=True)


