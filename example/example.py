# !python3


# Request
import requests 
import json
import pprint

# Hacer una llamada a la URL
url = 'http://hp-api.herokuapp.com/api/characters/house/gryffindor'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explorar la estructura de datos
resp_dict = r.json()
pprint.pprint(resp_dict[1]['name'])

bb = 'name' in resp_dict.keys()
print(bb)


# Por cada objeto sacar clave['nombre] y su valor.
#for i in range(3):
    #for name, value in resp_dict[i].items():
        #print(f"The key is {name} and the value is {value} ")

    
    

#readble_file = 'data/readable_hp_data.json'
#with open(readble_file, 'w') as f :
#    json.dump(resp_dict, f, indent=4) 
