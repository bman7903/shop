from mong import dump, idc, deld

bdb='baddb'

def empty( db ):
  g = str( dump( db ) )
  for e in g.split(' "_id" : { '):
     e = str( e )
     e = str( e.split(',')[0] )
     e = str( e.split('" : "')[-1] )
     if '"' in e:
       e = e.split('"}')[0]
       deld( db, e )

empty( db=bdb )
