# !python3
# class_api.py - Call the api and download the json to process it.


# Request - Module
import requests, json, pprint
import logging
logging.basicConfig(filename="log/myProgramLog.log",level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


class Api:
    def __init__(self):
        self.url = 'http://hp-api.herokuapp.com/api/characters/house/gryffindor'
        
    def request_data(self):
        try:  
            logging.info("Download data from URL")
            
            # Call to our URL
            req = requests.get(self.url)
            logging.info(f"Status code: {req.status_code}")
            
            # Getting our json data
            data = req.json()
            #pprint.pprint(data)
            
            
            # For each item in our dictionary we need extract:
                    # [name,gender, dateOfBirth, hairColour, species, house, wizard, hogwartsStudent, ancestry, wand, image]
            arr = []
            for item in data:
                obj = {
                    'name' : item['name'],
                    'gender': item['gender'],
                    'date_of_birth': item['dateOfBirth'],
                    'hair_colour' : item['hairColour'],
                    'species' : item['species'],
                    'house' : item['house'],
                    'wizard' : item['wizard'],
                    'hogwarts_student' : item['hogwartsStudent'],
                    'ancestry' : item['ancestry'],
                    'wand' : item['wand'],
                    'image' : item['image']        
                }
                arr.append(obj)
            #pprint.pprint(arr)
            
            
            
            # TODO: pasar todos los header a la funcion de 'class_exel' -> procesar datos
            
            #  Write and save the data in document.
            logging.info('Saving in JSON file.')
            readble_file = 'data/readable_hp_data.json'
            with open(readble_file, 'w') as f :
                json.dump(data, f, indent=4) 
                
            
            return arr # This function return our data.
            
        except :
            logging.info('Error to download.')
        finally:
           logging.info('Download done.') 
        
        
