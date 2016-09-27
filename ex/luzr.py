from mong import dump
from re import sub

def luzer( uzer ):
  l = []
  c = ''
  b = ''
  d = ''
  e = ''
  uzer = str( uzer )
  for k in str( dump( uzer ) ).split(' : { "$oid" : '):
     k = str( k )
     for i in k.split(" , "):
       i = str( i )
       if 'item' in i:
         c = str( sub('item','',i) )
       if '"price" : ' in i:
         b = str( i.split(':')[-1] ).strip()
       if '"lts" :' in i:
         d = str( i.split(':')[-1] ).strip()
       if '"pcs" :' in i:
         e = str( i.split(':')[-1] ).strip()
     c = str( sub('"" : "','',c) )
     c = str( sub('" : ','',c) )
     c = str( sub('" "',' ',c) )
     c = str( sub('"}','',c) )
     c = str( sub('"} ]','',c) )
     c = str( sub(']','',c) )
     t = str( c + ' $' + b + ' ' + d + '_left-at_' + e + '-per' )
     if not t.startswith(' '):
        l.append(t)
  return l

#g = luzer( 'mrx' )
#for e in g:
#  print(e)
