"""
Imports
"""
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from colorama import Fore, Style, Back

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
    Function takes a user input, checks for non-empty input,
    assigns it to a variable task, assigns a timestamp to a
    variable timestamp, and appends the task, an initial status
    of 'Not Done', and the timestamp to the Google Spreadsheet.
    The function uses a while loop to check if the task the user has entered 
    is empty
    """
    while True:
        task = input(Fore.YELLOW + Style.BRIGHT + "Enter the task:\n" + Style.RESET_ALL)
        if task.strip():  # Check if the input is non-empty after removing leading/trailing whitespaces
            break
        else:
            print(Fore.RED + Style.BRIGHT + "Task cannot be empty. Please try again." + Style.RESET_ALL)
            return

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


def remove_task(worksheet):
    """
    Function that checks for any existing tasks, displays them,
    takes a user input and if a task exists with the corresponding
    number it is removed, the function contains a try/except block
    which is used to catch any errors
    """
    try:
        # Get all values in the worksheet
        values = worksheet.get_all_values()

        if len(values) <= 0:
            print("No tasks available.")
            return

        view_tasks(worksheet)

        # Prompt the user to choose a task
        choice = int(input(Fore.YELLOW + Style.BRIGHT + "Enter the number of the task to remove:\n" + Style.RESET_ALL))

        # Remove the chosen task
        if 1 <= choice <= len(values):
            task_to_remove = values[choice - 1][0]  # Adjust for 0-based indexing
            worksheet.delete_rows(choice)
            print(Fore.GREEN + Style.BRIGHT + f'Task "{task_to_remove}" removed from Google Spreadsheet.' + Style.RESET_ALL)
        else:
            print("Invalid choice. Please enter a valid number.")
    except Exception as e:
        print(f"Error: {e}")


def mark_task_as_done(worksheet):
        # Get all values in the worksheet
        values = worksheet.get_all_values()

        if len(values) <= 0:
            print("No tasks available.")
            return

        view_tasks(worksheet)

        # Prompt user to choose a task
        choice = int(input(Fore.YELLOW + Style.BRIGHT + "Enter the number of the task to mark as done: " + Style.RESET_ALL))

        if 1 <= choice <= len(values):
            task_to_mark_as_done = values[choice - 1][0]  # Adjust for 0-based indexing
            worksheet.update_cell(choice, 2, 'Done') 
            print(Fore.GREEN + Style.BRIGHT + f'Task "{task_to_mark_as_done}" marked as done in Google Spreadsheet.' + Style.RESET_ALL)
            print(task_to_mark_as_done)
        else:
            print(Fore.RED + Style.BRIGHT + "Invalid choice. Please enter a valid number." + Style.RESET_ALL)

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


# def main():
#     worksheet = authenticate_google_sheets()

#     if worksheet:
#         while True:
#             display_menu()
#             choice = input(Fore.WHITE + Style.BRIGHT + "Enter your choice:\n" + Style.RESET_ALL)
            
#             if choice == '1':
#                 add_task(worksheet)
#             elif choice == '2':
#                 view_tasks(worksheet)
#             elif choice == '3':
#                 remove_task(worksheet)
#             elif choice == '4':
#                 break


# main()
worksheet = authenticate_google_sheets()
mark_task_as_done(worksheet)