# !python3
# main.py - Wee trigger the process in this  module.


# Import modules
from class_api import Api # API
from class_inputs import Input_mysql_credentials # Inputs
from class_excel import Excel
from class_mysql import Mysql_connection
from pprint import pprint


# Download data from our url
api = Api() 
data = api.request_data()


# Insert the data in Excel
xlsx = Excel()
xlsx.processing_data(data)

#TODO : QUITAR EL COMENTARIO
#Input Credentials
# Store the host, database, user and password. 
#CREDENTIALS = Input_mysql_credentials()
#CREDENTIALS.displayInput()

#TODO : QUITAR EL COMENTARIO
# Connection with MySQL
"""mysql_auth = {'host': CREDENTIALS.host, 
              'database' : CREDENTIALS.database, 
              'user' : CREDENTIALS.user, 
              'password' : CREDENTIALS.password}"""

pprint(data)

#mysqlcn = Mysql_connection(mysql_auth['host'], mysql_auth['database'], mysql_auth['user'], mysql_auth['password'])  # Insert the arguments that the instance need.
mysqlcn = Mysql_connection()
mysqlcn.connection_mysql(data)





