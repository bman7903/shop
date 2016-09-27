from mong import pst 
from ath import flux
from time import time
from re import sub

from requests import post

def cname( proc, src, dst ):
  def append( src, dst ):
     uri = str( flux('uri') )
     uri = str( sub( 'DOMAIN', src, uri ) )
     uri = str( sub( 'IP', dst, uri ) )
     print( 'fetching %s' % uri )
     r = post( uri )
     rc  = str( r.status_code )
     rsp = str( r.content )
     print( rc, rsp )
  if proc == 'append':
     append( src, dst )


g = cname( 'append', 'http://things-n-stuff-1.appspot.com', 'http://things-n-stuff.crabdance.com' )
print g
