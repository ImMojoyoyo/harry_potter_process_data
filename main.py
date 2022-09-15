# !python3
# main.py - Wee trigger the process in this  module.


# Import modules
from class_api import Api # API
from class_inputs import Input_mysql_credentials # Inputs
from class_excel import Excel
#from class_mysql import Mysql_connection
from pprint import pprint


# Download data from our url
api = Api() 
data = api.request_data()


# Insert the data in Excel
xlsx = Excel()
xlsx.processing_data(data)


#Input Credentials
# Store the host, database, user and password. 
CREDENTIALS = Input_mysql_credentials()
CREDENTIALS.displayInput()


# Connection with MySQL
mysql_auth = {'host': CREDENTIALS.host, 
              'database' : CREDENTIALS.database, 
              'user' : CREDENTIALS.user, 
              'password' : CREDENTIALS.password}


#mysqlcn = Mysql_connection(mysql_auth['host'], mysql_auth['database'], mysql_auth['user'], mysql_auth['password'])  # Insert the arguments that the instance need.
#mysqlcn.connection_mysql()


# TODO: Insert the data in Mysql database.





