# !python3
# class_mysql.py - Create the connection to our mysql service.

# Mysql modules
from pprint import pprint
import mysql.connector
from mysql.connector import Error

# Loggin module
import logging
logging.basicConfig(filename="myProgramLog.log",level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

class Mysql_connection :
   
   # Function that takes all the credentials to creat a connection. 
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    # Function that create the connection.
    def connection_mysql(self, data):
        #Create the connection to our mysql service.
        try:
            
            # Connectio to our DATABASE
            logging.info("Trying to connect...")
            print("Trying to connect...")
            CONNECTION = mysql.connector.connect(host = self.host, 
                                                 database = self.database, 
                                                 user = self.user, 
                                                 password = self.password)
                            
            # If you are connected to the database.                          
            if CONNECTION.is_connected():
                
                #TODO : Querie to create our table
                
                
                # Get the info of our database.
                db_Info = CONNECTION.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                
                # Get the info of our tables.
                cursor = CONNECTION.cursor()
                cursor.execute("select database();") # Show the database that we're connected.
                record = cursor.fetchone() # Store the data of our selection
                print("You're connected to database: ", record)
                
                # Show tables
                cursor.execute('show tables;')
                tables = cursor.fetchone()
                print('Our tables')
                pprint(tables)
                
                # Executing querie
                #cursor.execute();
                
                # TODO: Getting data to insert in database
                print('Our API Data:')
                #pprint(data)
                
                # Insert data in rows.
                hp_data = [] 
                for v in data:
                    name = v['name']
                    gender = v['gender']
                    date_of_birth = v['date_of_birth']
                    hair_colour = v['hair_colour']
                    species = v['species']
                    house = v['house']
                    wizard = v['wizard']
                    hogwarts_student = v['hogwarts_student']
                    ancestry = v['ancestry']
                    wand = str(v['wand'])
                    image = str(v['image'])
                    hp_data.append([name, gender, date_of_birth, hair_colour, species, house, wizard, hogwarts_student, ancestry, wand, image])
                pprint(hp_data)
                
                
                # Insert Data
                # TODO: For each item in hp_data we need do this.
                sql = "INSERT INTO user  VALUES (%s, %s)"
                val = ("Sergi", "Sarrió Vila")
                cursor.execute(sql, val)
                
                # Commit to save the data in database
                CONNECTION.commit()
                print(cursor.rowcount, 'Filled row')
 
        except Error as e:
            print("Err while try to connect", e)
            logging.error(f"Error with the database {e}")
            
        finally:
            if CONNECTION.is_connected():
                cursor.close()
                CONNECTION.close()
                logging.info("MySQL connection is close!")
    
    
    
    