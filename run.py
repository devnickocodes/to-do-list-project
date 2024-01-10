"""
Imports
"""
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from colorama import init, Fore, Style, Back
from pyfiglet import figlet_format 


# Initialize colorama
init()

class GoogleSheetValidator:
    SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
        ]


    def __init__(self, creds_file='creds.json', spreadsheet_name='to-do-list-app'):
        self.creds_file = creds_file
        self.spreadsheet_name = spreadsheet_name
        self.worksheet = self.authenticate_google_sheets()
        
        
    def authenticate_google_sheets(self):
        """
        Function that deals with authentication, access and retieval
        of Google Sheets spreadsheet for the tasks, it includes
        a try - except block that handles the issues if any in the
        authentication process arise and finally returns the retrieved spreadsheet
        """
        try:
            CREDS = Credentials.from_service_account_file(self.creds_file)
            SCOPED_CREDS = CREDS.with_scopes(self.SCOPE)
            GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
            SHEET = GSPREAD_CLIENT.open(self.spreadsheet_name)
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

    timestamp = datetime.now().strftime('%d-%m-%Y %H:%M')
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
            print(Fore.RED + Style.BRIGHT + "No tasks available." + Style.RESET_ALL)
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
            print(Fore.RED + Style.BRIGHT + "Invalid choice. Please enter a valid task number." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + f"Error: {e}" + Style.RESET_ALL)


def mark_task_as_done(worksheet, status = 'Done'):
    """
    Function that checks for any existing tasks, displays them,
    takes a user input and if a task exists with the corresponding
    number it is marked as done by updating the appropriate cell,
    the function contains a try/except block which is
    used to catch any errors
    """
    try:
        # Get all values in the worksheet
        values = worksheet.get_all_values()

        if len(values) <= 0:
            print("No tasks available.")
            return

        view_tasks(worksheet)

        # Prompt user to choose a task
        choice = int(input(Fore.YELLOW + Style.BRIGHT + f"Enter the number of the task to mark as {status}:\n" + Style.RESET_ALL))

        # Mark the chosen task as done
        if 1 <= choice <= len(values):
            task_to_mark_as_done = values[choice - 1][0]  # Adjust for 0-based indexing
            worksheet.update_cell(choice, 2, status) 
            print(Fore.GREEN + Style.BRIGHT + f'Task "{task_to_mark_as_done}" marked as {status} in Google Spreadsheet.' + Style.RESET_ALL)

        else:
            print(Fore.RED + Style.BRIGHT + "Invalid choice. Please enter a valid task number." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + f"Error: {e}" + Style.RESET_ALL)


def mark_task_as_not_done(worksheet):
    """
    Function that checks for any existing tasks, displays them,
    takes a user input and if a task exists with the corresponding
    number it is marked as not done by updating the appropriate cell,
    the function contains a try/except block which is
    used to catch any errors
    """
    mark_task_as_done(worksheet, status = 'Not Done')
    


def display_menu():
    """
    Function that displays the menu with the available
    options for the To-Do List to the user
    """
    #The menu display is inspired by Shaun Halverson's YouTube video
    
    print(Fore.CYAN + Style.BRIGHT)
    print("\n===== To-Do List App =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Mark Task as Not Done")
    print("6. Quit")
    print("=========================")
    print(Style.RESET_ALL)

def title_text():
    """
    Function that displays the styled intro and author texts
    """
    intro = figlet_format("Welcome to your To-Do List !", font = "mini", width = 70, justify = 'center')
    author = figlet_format("By Nikolay Hristev", font = "contessa", width = 80, justify = 'center')
    
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + intro)
    print(author + Style.RESET_ALL)

def main():
    """
    Function that combines all the other main functions
    that operate the app. Prints the intro message 
    retrieves and validates the Google Spreadsheet, takes
    user input and based on that input it invokes the 
    necessary function. 
    """

    title_text()
    worksheet = authenticate_google_sheets()

    if worksheet:
        while True:
            display_menu()
            choice = input(Fore.WHITE + Style.BRIGHT + "Enter your choice (1-6):\n" + Style.RESET_ALL)
            
            if choice == '1':
                add_task(worksheet)
            elif choice == '2':
                view_tasks(worksheet)
            elif choice == '3':
                remove_task(worksheet)
            elif choice == '4':
                mark_task_as_done(worksheet)
            elif choice == '5':
                mark_task_as_not_done(worksheet)
            elif choice == '6':
                print(Fore.LIGHTBLUE_EX + "Thanks for using the To-Do List App!")
                print("Goobye!" + Style.RESET_ALL)
                break
            else:
                print(Fore.RED + Style.BRIGHT + "Invalid choice. Please enter a number between 1 and 6." + Style.RESET_ALL)


main()
