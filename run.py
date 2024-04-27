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

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('coctail_quiz')

def get_sales_data():
    """
    Get sales figures input from user
    """
    while True:
        print("Please enter sales dta from last market.")
        print("Data should be six numbers,separetedseparated by commas.")
        print("Example:10,20,30,40,50,60\n")

        data_str = input("Enter your data here:")
    
        sales_data = data_str.split(",")
        print(sales_data)

        if validate_data(sales_data):
            print("Data is valid!")
            break
    return sales_data

def validate_data(values):
    """
    Get sales figure input from user.
    Run a while loop to collect valid string of data from user via terminal, 
    which must be a string of 6 numbers separeted by commas. 
    The loop will repetedely request data,until it is valid. 
    """
    try:
        [int(value)for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required,you provided {len(values)}"
            )
    except ValueError as e:
        print("Invalid data: {e},please try again.\n")
        return False
    return True

def update_sales_worksheet(data):
    """
    Update sales worksheet,
    add new row with the list data provided.
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet update succesfully.\n")


data = get_sales_data()
sales_data = [int(num) for num in data]
update_sales_worksheet(sales_data)