from os import listdir
from random import choice

idir = 'img'

def rpic( dir, query ):
  query = str( query )
  if query == 'None':
     dir = str( idir + '/' + str( dir ) )
     e   = listdir( dir )
     ic  = str(  dir + '/' + str( choice( e ) ) )
     return ic
  q   = ['None']
  dir = str( idir + '/' + str( dir ) )
  e   = listdir( dir )
  for i in e:
     i = str( i )
     if query in i:
       q.append(i)
  c   = str( choice( q ) )
  if c == 'None':
     return c
  ic  = str(  dir + '/' + c )
  return ic


e=rpic('monkey','None')
print(e)
