#!/usr/bin/python

from binascii import hexlify, unhexlify
from sys import argv, exit
import pyelliptic
from os import path

exist = path.exists
g     = []

try:
  proc  = str( argv[1] )
  fle   = argv[2]
except:
  print( 'Usage:   ./ec.py "c|d" file' )
  exit()

if exist( fle ):
  a     = open( fle, 'r' )
  for b in a.readlines():
     b = str( b )
     g.append( b )
  iv = pyelliptic.Cipher.gen_IV('aes-256-cfb')
  iv = 'frogsareprettycool'


  if 'c' in proc:
     ctx = pyelliptic.Cipher("secretkey", iv, 1, ciphername='aes-256-cfb')
#     print( ctx ) 
     for e in g:
       try:
         ciphertext += ctx.update(e)
       except:
         ciphertext = ctx.update(e)
     ciphertext += ctx.final()
     ciphertext = hexlify( ciphertext )
     print( ciphertext )
  else:
     ctx2 = pyelliptic.Cipher("secretkey", iv, 0, ciphername='aes-256-cfb')
     for e in g:
       try:
          ciphertext += e
       except:
          ciphertext = e
     ciphertext = str( ciphertext ).strip()
     ciphertext = unhexlify( ciphertext )
     print(ctx2.ciphering( ciphertext ))
else:
  print( 'file not found' )
  exit()

# Asymmetric encryption
#alice = pyelliptic.ECC() # default curve: sect283r1
#bob = pyelliptic.ECC(curve='sect571r1')

#ciphertext = alice.encrypt("Hello Bob", bob.get_pubkey(),
#                           ephemcurve='sect571r1')
#print(bob.decrypt(ciphertext))

#signature = bob.sign("Hello Alice")
# alice's job :
#print(pyelliptic.ECC(pubkey=bob.get_pubkey(),
#                     curve='sect571r1').verify(signature, "Hello Alice"))

# ERROR !!!
#try:
#    key = alice.get_ecdh_key(bob.get_pubkey())
#except:
#    print("For ECDH key agreement, the keys must be defined on the same curve !")

#alice = pyelliptic.ECC(curve='sect571r1')
#print(hexlify(alice.get_ecdh_key(bob.get_pubkey())))
#print(hexlify(bob.get_ecdh_key(alice.get_pubkey())))
