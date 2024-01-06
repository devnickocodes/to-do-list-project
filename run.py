"""
Imports
"""
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from colorama import Fore, Style

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


def authenticate_google_sheets():
    """
    Function that deals with authentication, access and retieval
    of Google Sheets spreadsheet for the tasks, it includes
    a try - except block that handles the issues if any in the
    authentication process arise and finally returns the retrieved spreadsheet.
    """
    try:
        CREDS = Credentials.from_service_account_file('creds.json')
        SCOPED_CREDS = CREDS.with_scopes(SCOPE)
        GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
        SHEET = GSPREAD_CLIENT.open('to-do-list-app')
        worksheet = SHEET.get_worksheet(0) 
        return worksheet
    except Exception as e:
        print(f"Error: {e}")
        return None


def view_tasks(worksheet):
    """
    Function that checks for available tasks with an if statement
    and using a for loop it displays all the available tasks 
    in the specified format by the f-string
    """
    # Get all values in the worksheet
    values = worksheet.get_all_values()

    if len(values) <= 0:
        print("No tasks available.")
    else:
        print("\nTasks:\n")
        for i, row in enumerate(values, 1):
            print(f"{i}. {row[0]} - Status: {row[1]}, Timestamp: {row[2]}")


def display_menu():
    """
    Function that displays the menu with the available options for the To-Do List to the user
    """
    print(Fore.CYAN + Style.BRIGHT + "\n===== To-Do List App =====")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Mark Task as Done")
    print("5. Quit")
    print("=========================" + Style.RESET_ALL)


def validate():
    display_menu()
    worksheet = authenticate_google_sheets()
    view_tasks(worksheet)
    

validate()
