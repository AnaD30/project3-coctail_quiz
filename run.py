# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials 
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
    
    CREDS = Credentials.from_service_account_file('creds.json')
    SCOPED_CREDS = CREDS.with_scope(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GSPREAD_CLIENT.open('coctail_game')

def get_sales_data():
    """
    Get sales figures input from user
    """
    print("Please enter sales dta from last market.")
    print("Data should be six numbers,separetedseparated by commas.")
    print("Example:10,20,30,40,50,60\n")

    data_str = input("Enter your data here:")
    print(f'The data provided is{data_strg}')

get_sales_data()