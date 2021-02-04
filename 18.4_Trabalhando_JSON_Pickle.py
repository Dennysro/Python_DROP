"""
JSON e Pickle

JSON -> Java Script Object Notation
API -> Meios de comunicação entre os serviços oferecidos por empresas
(Twitter, facebook, Youtube) e terceiros (Nós desenvolvedores)


"""

import json

ret = json.dumps(['produto', {'Playstation 4': ('2TB', 'Novo', '220V', 2340)}])
print(type(ret))
print(ret)



