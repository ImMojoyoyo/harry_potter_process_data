# !python3 
# class_excel.py - This module build a workbook for an exel and insert the data inside this workbook.


# Modules
from pprint import pprint
from typing import final
import openpyxl

# Loggin module
import logging
logging.basicConfig(filename="myProgramLog.log",level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

class Excel:
    
    def __init__(self):
        self.name = ""
    
        
    # Processing data & create and Excel file   
    def processing_data(self, data):
        try:
            logging.info('Creating excel...')
            # Create our excel
            print('Creating excel...')
            wb = openpyxl.Workbook() # Create a blank workbook
            
            
            # Create our sheet.
            sheet = wb.active
            sheet.title = 'harry_potter_characters'
            print(wb.sheetnames)
            
            
            # Insert headers in our worksheet.
            
            
            header_keys_excel = [] #Store the keys of our JSON 
            # Take the keys of our paramethers data.
            for k in data[0].keys():
                header_keys_excel.append(k.title())
            print(header_keys_excel)
            
            # Insert the headers.
            for index, value in enumerate(header_keys_excel):
                sheet.cell(1, index + 1).value = value
            
            # Insert the content.
            pprint(data)
                
            

            
            # TODO: Save our workbook
                # TODO: Change the title
            wb.save('excel/harry_potter_analysis.xlsx')
            
        except:
            logging.error('Err creating the excel')
        finally:
            logging.info('Excel create succesfully!')
              
        
        
        
        
