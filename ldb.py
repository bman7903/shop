from mong import dump
from random import shuffle
from re import sub

def rselect( udb ):
  lz = []
  zl = ''
  x  = 1
  for e in str( dump( udb ) ).split('_id" : {'):
     e = str( e )
     oid  = User = item = img1 = 'None' 
     for f in e.split(' , '):
       f  = str( f )
       f  = str( sub( '"','', f ) )
       h  = str( f.split(' : ')[0] ).strip()
       g  = str( f.split(' : ')[-1] ).strip()
       gl = ( len( g ) - 1 )
       h  = str( h.strip('"') )
       if '$oid' in h:
          oid = str( g[0:gl] )
       if 'User' in h:
          User = str( sub(']','',g) ).strip()
          lu   = ( len( User ) - 1 )
          User = str( User[0:lu] )
       if 'item' in h:
          item = g
       if 'img1' in h:
          img1 = g
       v = str( oid + '_' + User + '-' + item )
       mok = str( '<td><form action="/lot" method="post" style="display:inline"><input type="hidden" name="oid" value="' + v + '">'\
       + '<input id="unpressed" type="submit" value=" " name="' + v + '" style="background:url(' + img1 + '); display:inline; width:128px; height:128px;   background-size: 100%; no-repeat;border:none; background-size: cover;"/></form>&nbsp&nbsp' )
       if not 'None' in mok:
          z  = str( lz )
          if not mok in z:
            lz.append( mok )
  shuffle(lz)
  for e in lz:
     if x == 1:
       e = str( '<div>' + e )
     try:
       if x % 4 == 0:
          e = str( e + '</div><br><div>' )
     except:
       pass
     zl = str( zl  + e )
     x = ( x + 1 )
  zl = str( '<center>' + zl + '</center>' )
  return zl

#e = rselect( 'masterdb' )
#print e
