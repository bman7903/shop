from mong import pst 
from ath import mlab
from time import time
from socket import inet_aton, inet_ntoa
from struct import pack, unpack


mongolab_key = str( mlab('mkey') )
k_db      = str( mlab('k_db') )

def ip2long( ip ):
    vert = inet_aton( ip )
    return unpack( '!L', vert)[0]

def long2ip( ip ):
  ip = int( ip )
  vert = inet_ntoa( pack( '!L', ip ) )
  return vert

def cvert( ip ):
     ### IP dec 10 xor 255
     i = str( ip )
     if '.' in i:
       vert = ip2long( ip )
     else:
       vert = long2ip( ip )
     return vert

def addto( ip, guid, iid ):
  krt  = str( cvert( ip ) )
  guid = str( guid )
  tme = str( time() ).split('.')[0]
  Data = [
     {
       'kart':krt,
       'guid':guid,
       'iid':iid,
       'time':tme,
     }
  ]
  pst( k_db, Data )


def knt( ip, proc ):  
  ### kart operations
  ltz  = []
  proc = str( proc )
  krt  = str( vert( ip ) )
  for e in dump( k_db ):
     e = str( e )
     if krt in e:
        ltz.append( e )
  lt = len( ltz )

  if proc == 'count':
    if lt < 1:
       return False
    else:
       return True

  if proc == 'dump':
    if lt > 0:
       return ltz
    else:
       return None
