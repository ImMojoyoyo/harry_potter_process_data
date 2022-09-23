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
    def connection_mysql(self):
        #Create the connection to our mysql service.
        try:
            logging.info("Trying to connect...")
            print("Trying to connect...")
            # Credentials
            CONNECTION = mysql.connector.connect(host = self.host, 
                                                 database = self.database, 
                                                 user = self.user, 
                                                 password = self.password)
            
            
            # Querie
            mysql_querie_create_table = """ CREATE TABLE harry_potter_character ( 
                                        id int(11) NOT NULL,
                                        name varchar(250) NOT NULL,
                                        gender varchar(15) NOT NULL,
                                        date_of_birth varchar(15) NOT NULL,
                                        hair_colour varchar(20) NOT NULL,
                                        species varchar(20) NOT NULL,
                                        house varchar(50) NOT NULL,
                                        wizard varchar(10) NOT NULL,
                                        hogwarts_student varchar(10) NOT NULL,
                                        ancestry varchar(15) NOT NULL,
                                        wand varchar(200) NOT NULL,
                                        image varchar(200) NOT NULL,                                    
                                        PRIMARY KEY (Id))  """
                                        
                                        
                                        
            if CONNECTION.is_connected():
                
                # Get the info of our database.
                db_Info = CONNECTION.get_server_info()
                logging.info("Connected to MySQL Server version ", db_Info)
                
                # Get the info of our tables.
                cursor = CONNECTION.cursor()
                cursor.execute("select database();") # Show the database that we're connected.
                record = cursor.fetchone()
                logging.info("You're connected to database: ", record)
                
                cursor.execute('show tables;')
                tables = cursor.fetchone()
                pprint(tables)
                
                # TODO: Check if our database have tables or not.
                if tables == None:
                    cursor.execute(mysql_querie_create_table)
                    pprint('Table created!')
                else:
                    pprint('We have tables')
                    
                # TODO: Create new queries
                    
                # Trigger a querie to our database.
                #cursor.execute("DROP TABLE User;")
                #result = cursor.execute(show_tables)
                #print(result)
                
                
            
        except Error as e:
            print("Err while try to connect", e)
            logging.error(f"Error with the database {e}")
            
        finally:
            if CONNECTION.is_connected():
                cursor.close()
                CONNECTION.close()
                logging.info("MySQL connection is close!")
    
    # Function 'insert data' in database.      
    def insert_data():
        try:
            logging.info("Inserting data in database...")
        
        except:
            logging.error("Inserting data in database FAILED")
        
        finally:
            logging.info("Finished process insert data in database.")
            logging.info('Succes!')