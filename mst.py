from mong import dump
from re import sub
from itertools import groupby

mstr='masterdb'


def mdump( proc ):
  proc = str( proc )
  def all():
     t = str( dump( mstr ) )
     g = str( sub('}','',t) )
     g = str( sub('{','',g) )
     g = str( sub('"_id"','',g) )
     g = str( sub('   :  ','',g) )
     return g
  All = str( all() )
  def gory():
     g = []
     for e in All.split(' , '):
       e = str( e )
       if 'gory' in e:
          le = int( len(e) - 1 )
          e  = e[10:le]
          g.append( e )
     return g
  def greatgory():
     g   = gory()
     lim = 1
     l   = []
     t   = []
     f   = [len(list(group)) for key, group in groupby(g)]
     for e in f:
       if e > lim:
         l.append(e)
     if l > 0:
        for e in l:
          j = g[e]
          t.append( j )
     return t

  def greatdoc():
     g = greatgory()
     i = []
     m = 6
     if len( g ) > 0:
       for j in g:
          j = str( j )
          for e in All.split('$oid'):
            e = str( e )
            print e 
            k = str( '"gory" : ' + j )
            if k in e:
              li = len( i )
              if le < m:
                  i.append( e )
     return i

  t = eval( proc )
  return t()


for e in mdump('gory'):
  print(e)
  print
#for a in e:
#  print( a )
#le = len( e )
#print le
