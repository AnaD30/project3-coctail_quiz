# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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

def update_worksheet(data,worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with data provided
    """
    print("Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet}worksheet upadete succsuccessfully\n")

def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus from each item type.

    The surplus is defined as the sales figure subtarcted from the stock:
    -Positive surplis indicate waste
    -Negative surplus indicates extra made when stock was sold out.
    """
    print("calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]

    surplus_data = []
    for stock,sales in zp(stock_row,sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    
    return surplus_data
def get_last_5_entries_sales(sales):
    """
    Collects columms of data from sales worksheet,
    collecting the last 5 entries for each coctail 
    and returns the data as a lsit of lists. 
    """
    sales = SHEET.worksheet("sales")
   
    columns = []
    for ind in range(1,7):
        columns = sales.col_values(ind)
        columns.append(columns[-5:])
    return columns

def main():
    """
    Run program functions
    """
data = get_sales_data()
sales_data = [int(num) for num in data]
update_worksheet(sales_data,"sales")
new_surplus_data = calculate_surplus_data(sales_data)
update_worksheet(new_surplus_data,"surplus")

print("Welcome to Coctail Data Automation")
#main()
sales_columns = get_last_5_entries_sales()
