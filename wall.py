from mong import dump, pst, deld, idc

def wall( baddb, proc, ip ):
  baddb = str( baddb )
  proc  = str( proc )
  ip    = str( ip )
  g     = ''

  def check( baddb, ip ):
     g = str( dump( baddb ) )
     for e in  g.split(', { "_id" : '):
       e = str( e )
       if ip in e:
          return True
     return False

  def add( baddb, ip ):
     stuff = [ { "ip":ip } ]
     g = pst( baddb, stuff )
     return g

  def remove( baddb, ip ):
     id = str( idc( baddb, 'ip', ip ) )
     print(id)
     g = deld( baddb, id )
     print(g)
     return g

  if proc == 'check':
    g = check( baddb, ip )
  if proc == 'add':
    g = add( baddb, ip )
  if proc == 'remove':
    g = remove( baddb, ip )
  return g




#baddb = 'baddb'
#proc  = 'remove'
#ip    = '6.6.6.6'
#g = wall( baddb, proc, ip )
#print(g)


#fetz = str( wall( baddb, 'check', ip ) )
#print( fetz )
#if 'True' in fetz:
#  print( 'Removing ' + ip )
#  wall( baddb, 'remove', ip )
#if 'False' in fetz:
#  print( 'Adding ' + ip )
#  wall( baddb, 'add', ip )
#print(g)
