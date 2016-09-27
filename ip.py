#!/usr/bin/env python

from socket import inet_aton, inet_ntoa
from struct import pack, unpack
from sys import argv

def ip2long( ip ):
    vert = inet_aton( ip )
    return unpack( '!L', vert)[0]

def long2ip( ip ):
  ip = int( ip )
  vert = inet_ntoa( pack( '!L', ip ) )
  return vert

def cvert( ip ):
     i = str( ip )
     if '.' in i:
       vert = ip2long( ip )
     else:
       vert = long2ip( ip )
     return vert

z = cvert( ip=argv[1] )
print(z)
