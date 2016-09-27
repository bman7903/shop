from mong import dump, lstc
from re import sub

def retc( User, doc ):
  g = str( lstc( User, doc ) )
  g = str( sub('}','',g) )
  g = str( sub('{','',g) )
  g = str( sub(' "_id" :','',g ) )
  print g


User = 'mrx'
oid  ='56840f82e4b0c43796c61a0e'
retc( User, oid )
