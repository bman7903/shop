import requests

data       =   [{"eleven":"twelve","thirteen":"fourteen"}]
headers    =   {"Content-Type": "application/json"}

doc='56793adee4b0605936f19247'
dta="https://api.mongolab.com/api/1/databases/tmpusr/collections/rick/" + doc + "?apiKey="
r = requests.delete(dta, headers=headers, data=data)

sc = str( r.status_code )
rc = str( r.text )

print( sc + '\n' + rc + '\n' + sc )
