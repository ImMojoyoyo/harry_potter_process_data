# !python3
# class_inputs.py - Module that catch the credentials of our database connection.

class Input_mysql_credentials:
    
    # Function that store all the credentials.
    def __init__(self):
        self.host = input("Type the HOST of your database: ")   
        self.database = input("Type the NAME of your database: ") 
        self.user = input("Type the USER of your database: ") 
        self.password = input("Type the PASSWORD of your database: ") 
     
     
    def displayInput(self):
        print(f"The host is: {self.host}, the name is {self.database}, the user is {self.user} and the password is {self.password}")