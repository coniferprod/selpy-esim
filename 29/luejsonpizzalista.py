import json

with open('pizzalista.json') as tiedosto:
    pizzat_json = json.load(tiedosto)

pizzat = {}
for k in pizzat_json.keys():
    p = pizzat_json[k]
    ik = int(k)
    pizzat[ik] = {'nimi': p['nimi'],
                  'taytteet': set(p['taytteet'])}

import pprint
pprint.pp(pizzat)
