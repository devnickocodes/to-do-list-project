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
    Function that deals with authentication and access
    to Google Sheets spreadsheet for the tasks, it includes
    a try - except block that handles the issues if any in the
    authentication process arise
    """
    try:
        CREDS = Credentials.from_service_account_file('creds.json')
        SCOPED_CREDS = CREDS.with_scopes(SCOPE)
        GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
        SHEET = GSPREAD_CLIENT.open('to-do-list-app')
        tasks = SHEET.get_worksheet(0) 
        worksheet = tasks.get_all_values()
        return worksheet
    except Exception as e:
        print(f"Error: {e}")
        return None


def validate():

    worksheet = authenticate_google_sheets()
    print(worksheet)


validate()