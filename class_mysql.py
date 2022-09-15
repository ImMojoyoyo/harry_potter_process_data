# !python3
# class_mysql.py - Create the connection to our mysql service.

# Mysql modules
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
            mysql_querie_create_table = """CREATE TABLE User ( 
                                        Id int(11) NOT NULL,
                                        Name varchar(250) NOT NULL,
                                        Lastname varchar(3) NOT NULL,
                                        Phone varchar(9) NOT NULL,
                                        PRIMARY KEY (Id)) """
                                        
                                        
                                        
            if CONNECTION.is_connected():
                
                # Get the info of our database.
                db_Info = CONNECTION.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                
                # Get the info of our tables.
                cursor = CONNECTION.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)
                
                # Trigger a querie to our database.
                #cursor.execute("DROP TABLE User;")
                result = cursor.execute(mysql_querie_create_table)
                print(result)
                
                
            
        except Error as e:
            print("Err while try to connect", e)
            logging.error(f"Error with the database {e}")
            
        finally:
            if CONNECTION.is_connected():
                cursor.close()
                CONNECTION.close()
                logging.info("MySQL connection is close!")
            
        