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
    authentication process arise and finally returns the retrieved spreadsheet
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


def add_task(worksheet):
    """
    Function takes a user input and assigns it to a variable task,
    assigns a timestamp to a variable timestamp and appends the
    task, an initial status of 'Not Done' and the timestamp to
    the Google Spreadsheet
    """
    task = input(Fore.YELLOW + Style.BRIGHT + "Enter the task:\n" + Style.RESET_ALL)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Append task data to the Google Spreadsheet
    worksheet.append_row([task, 'Not Done', timestamp])
    print(Fore.GREEN + Style.BRIGHT + f'Task "{task}" added to Google Spreadsheet.' + Style.RESET_ALL)


def view_tasks(worksheet):
    """
    Function that checks for available tasks with an if statement
    and using a for loop it displays all the available tasks
    in the specified format by the f-string
    """
    # Get all values in the worksheet
    values = worksheet.get_all_values()

    if len(values) <= 0:
        print(Fore.RED + Style.BRIGHT + "No tasks available." + Style.RESET_ALL)
    else:
        print(Fore.MAGENTA + Style.BRIGHT + "\nTasks:\n" + Style.RESET_ALL)
        for i, row in enumerate(values, 1):
            print(Fore.MAGENTA + Style.BRIGHT + f"{i}. {row[0]} - Status: {row[1]}, Timestamp: {row[2]}" + Style.RESET_ALL)


def display_menu():
    """
    Function that displays the menu with the available
    options for the To-Do List to the user
    """
    print(Fore.CYAN + Style.BRIGHT)
    print("\n===== To-Do List App =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Quit")
    print("=========================")
    print(Style.RESET_ALL)


def main():
    worksheet = authenticate_google_sheets()

    if worksheet:
        while True:
            display_menu()
            choice = input(Fore.WHITE + Style.BRIGHT + "Enter your choice:\n" + Style.RESET_ALL)
            
            if choice == '1':
                add_task(worksheet)
            elif choice == '2':
                view_tasks(worksheet)
                break


main()
