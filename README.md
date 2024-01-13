# The To-Do List App
![To-Do List App Overview](https://github.com/devnickocodes/to-do-list-project/blob/main/documentation/to-do-list-app-overview.png)

You can find the deployed project live link [HERE](https://to-do-app-project-d0d8633fbefc.herokuapp.com/)

## Introduction

The To-Do List App provides the user with an easy way to keep track of their tasks. The app provides the user with all the necessary options that are needed to manage their tasks. Including creating a task, viewing their tasks, removing a task, and more. The user can do everything from the terminal. The app is deployed on Heroku using Code Institute's mock terminal template. If a user tries to remove or mark a task as done that doesn’t exist they will be shown the menu again and they could reselect the option or choose a different one. The user is provided with the option of marking a task as undone if they have made a mistake or changed their mind.

## Project 

The objective of this project is to:

- Allow the user to conveniently manage their tasks.
- Allow the user to add as many tasks as they would like.
- Allow the user to keep track of the status of their tasks.
- Allow the user to remove any task they would like.
- Allow the user to change the status of their tasks from Not Done to Done and vice versa as many times as they would like.
- Allow the user to see the timestamps for their task was created.
- Allow the user to exit the app.

### User goals:

- Clearly see the intro and author of the app.
- Add a task to a Google Spreadsheet.
- View the added tasks in the Google Spreadsheet if there are any.
- Remove any task I want.
- Mark any task as Done and update the status of the task in the Google Spreadsheet.
- Mark any task as Not Done and update the status of the task in the Google Spreadsheet.
- See when the task was created.
- Quit the app.

### Creator Goals:

- Create a program which will be useful to a lot of people and is easy to maintain. 
- Create a program that is flexible and allows changes and additional options to be added if needed.
- Create a program that is easy to use, and straightforward to navigate around.

### Pre development

I created a flowchart to use as guidance and break the code into smaller steps, this way I had a clear idea of what I needed to implement. The flowchart shows the logic that the app uses depending on which option is given. The inputs that it is asking from the user as well as the operations it will perform based on those inputs, as well as how the program handles a task number that doesn’t exist, or if a letter is given instead of an integer number.

![To-Do List App Flowchart](https://github.com/devnickocodes/to-do-list-project/blob/main/documentation/to-do-list-flowchart.png)

### Development

After writing some of the code I was using the os module and while it was working perfectly fine in the terminal for creating .txt files that would store the tasks. Upon deployment, nothing was happening. After getting in touch with tutor support they suggested that I implement Google Spreadsheet as a form of a database. I decided I would take this approach and began creating the project from scratch. There was ongoing testing throughout the whole creation of the project using `print` functions and checking truthy/falsy values with the `bool()` function. First, the code for retrieving and accessing Google Spreadsheet was written and then each function was written as needed. Upon further testing additional features were added that would deal with if the user provides a number that is outside the current range of the tasks list, try/except blocks were added that would take care of other errors for example if a user inputs a letter instead of an integer number. After the second meeting with my tutor, he suggested that I look into OOP, so I decided to include a class in the project that handles the authentication of the Google Spreadsheet, with another reason being that there are no variables in the global scope.

#### Invalid Input

- Add Task (Option - 1)

If the user tries to add an empty task they will be met with a message that says that the task cannot be empty and they will be redirected to the menu.

![Empty Task Input](https://github.com/devnickocodes/to-do-list-project/blob/main/documentation/enter-empty-task-add-task-option.png)

- Remove Task (Option - 3)

If the user tries to remove a non-existent task, they will be reminded that they need to choose a valid task number and they will be redirected to the menu.

![Non-existent Task Input](https://github.com/devnickocodes/to-do-list-project/blob/main/documentation/enter-a-non-existant-task-remove-task-option.png)

If the user tries to enter a letter, they will be show an error message which is part of the try/except block and they will be redirected to the menu.

![Letter Input](https://github.com/devnickocodes/to-do-list-project/blob/main/documentation/enter-a-letter-remove-task-option.png)

- Mark Task As Done (Option - 4)

If the user tries to mark a non-existent task as done, they will be reminded that they need to choose a valid task number and they will be redirected to the menu.

![Input for a non-existent task to mark as done](https://github.com/devnickocodes/to-do-list-project/blob/main/documentation/enter-a-non-existant-task-mark-task-as-done-option.png)

If the user tries to enter a letter, they will be show an error message which is part of the try/except block and they will be redirected to the menu.

![Letter Input](https://github.com/devnickocodes/to-do-list-project/blob/main/documentation/enter-a-letter-mark-task-as-done-option.png)

- Mark Task As Not Done (Option - 5)

If the user tries to mark a non-existent task as not done, they will be reminded that they need to choose a valid task number and they will be redirected to the menu.

![Input for a non-existent task to mark as not done](https://github.com/devnickocodes/to-do-list-project/blob/main/documentation/enter-a-non-existant-task-mark-task-as-not-done-option.png)

If the user tries to enter a letter, they will be show an error message which is part of the try/except block and they will be redirected to the menu.

![Letter Input](https://github.com/devnickocodes/to-do-list-project/blob/main/documentation/enter-a-letter-mark-task-as-not-done-option.png)

## Features 

### Add Task

This feature allows the user to create a task that will be stored in Google Spreadsheet. It logs the task in the first cell, creates a status variable with an initial status of ‘Not Done’ and logs it in the second cell, and finally creates a timestamp which is logged in the third cell of the spreadsheet. After that, the user is directed to the menu again.

![Add Task (Option - 1)](https://github.com/devnickocodes/to-do-list-project/blob/main/documentation/add-a-task.png)

### View Tasks

This feature retrieves all the available tasks with their statuses and timestamps and displays them to the user. After that, the user is directed to the menu again.

![View Tasks (Option - 2)](https://github.com/devnickocodes/to-do-list-project/blob/main/documentation/view-tasks.png)

### Remove Task

The next feature displays all the available tasks and takes a user input as to which task should be removed, if the task exists it is removed from the spreadsheet, if it doesn’t the user is directed to the menu again.

![Remove Task (Option - 3)](https://github.com/devnickocodes/to-do-list-project/blob/main/documentation/remove-task.png)

### Mark Task As Done 

This feature displays all the available tasks and takes user input as to which task should be marked as done. If the task exists the second cell for that task in the spreadsheet, which is the status cell is updated to ‘Done’ after which the user is directed to the menu again.

![Mark Task As Done (Option - 4)](https://github.com/devnickocodes/to-do-list-project/blob/main/documentation/mark-task-as-done.png)

### Mark Task As Not Done

This feature displays all the available tasks and takes user input as to which task should be marked as not done. If the task exists the second cell for that task in the spreadsheet, which is the status cell is updated to ‘Not Done’ after which the user is directed to the menu again.

![Mark Task As Not Done (Option - 5)](https://github.com/devnickocodes/to-do-list-project/blob/main/documentation/mark-task-as-not-done.png)

### Quit

This feature displays goodbye messages and stops the running of the app.

![Quit (Option - 6)](https://github.com/devnickocodes/to-do-list-project/blob/main/documentation/quit-option.png)

## Features Left To Implement

### Authentication

- Add a form of authentication so each user gets their own Google sheet and they can’t access each other’s.

### Download Tasks List

- add an option that allows the user to download the spreadsheet with their tasks on their computer.

## Technologies Used

Find the technologies used for this project below:

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

    - The project was developed using Python.

- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

    - JavaScript script was used to run Code Institute’s mock terminal

- [Github](https://github.com/)

    - For storage of the website's code as well as deployment, Github was used.

- [Git](https://git-scm.com/)

    - Git commands were used in the IDE for version control.

- [Gitpod](https://gitpod.io/) and [CodeAnywhere](https://codeanywhere.com/solutions/collaborate)

    - Gitpod and CodeAnywhere IDEs were used to write the code for this project, which will be pushed to GitHub with Git commands.

- [Google Spreadsheets](https://www.google.com/sheets/about/)

    - Google Spreadsheets is used to store the tasks' list.

- [Google Cloud Platform](https://console.cloud.google.com/)

    - Google Cloud Platform was used to enable the APIs for this project.

## Imported Libraries 

- [gspread](https://docs.gspread.org/en/v5.7.0/) was used to connect the project to Google Sheets to retrieve, read and update the tasks' list.
- [PyFiglet](https://pypi.org/project/pyfiglet/) was used for the intro and author sections at the beggining of the program.
- [Colorama](https://pypi.org/project/colorama/) was used for styling the terminal by changing the colors of the print functions.
- [Datetime](https://docs.python.org/3/library/datetime.html) was used for the timestamps of the tasks.
- [google-auth](https://google-auth.readthedocs.io/en/master/#google-auth) was used for secure authentication with Google APIs


## Testing 

## Bugs

Since I installed and imported the PyFiglet library after I had already started working on the project when I deployed the app and I was met with an error saying that the module was not found. After that I realised that I had forgotten to install the necessary dependancies in the requirements file, and after I did that the app was running with no issues.

![PyFiglet Module Error](https://github.com/devnickocodes/to-do-list-project/blob/main/documentation/pyfiglet-module-not-found-error.png)


## Validation

I imported [this](https://pypi.org/project/pep8/) python style checker.

I used the [CI Python Linter](https://pep8ci.herokuapp.com/) to validate the code. After removing some blank lines, whitespaces and adjusting lines that were too long the code passed the validation with no issues.

![CI Python Linter Validation](https://github.com/devnickocodes/to-do-list-project/blob/main/documentation/pep8-validator.png)

## Deployment

### Local Deployment

#### How to Fork

1. Sign Up or Log In if you have an account to Github.
2. Go to the repository for the To-Do List project - [devnickocodes/To-Do List Project](https://github.com/devnickocodes/to-do-list-project)
3. Click on the Fork button that is on the right side of the repository name.

#### How to Clone

You can make a local copy of The Elements Game project by writing the following command in your IDE terminal.

- `git clone https://github.com/devnickocodes/to-do-list-project.git` 

#### Heroku 

Heroku is used for the deployment of the project, here are the steps after you create your account:

1. Click on 'New' at the top-right corner of your Dashboard, then select 'Create new app'
2. Choose a distinct app name (as no two projects can have the same name on Heroku) and choose your region
3. Click on 'Create App' 
4. Navigate to 'Settings'
5. Click on 'Reveal Config Vars' 
6. In the input field of 'KEY' type in 'PORT' and in the input field of 'VALUE' type in '8000' 
7. You must also include (where applicable) private API key information. In the input field of 'KEY' type in 'CREDS', after that copy the private API contents of your .json file and paste them in the input field of 'VALUE'
8. Below the 'Config Vars' section, find the 'Buildpacks' (dependancies) section and click on 'Add buildpack'
9. The order of the buildpacks here is very important. First Add the Python buildpack and after that add the buildpack for Node.js (If they are in a different order, on the left side there are three bars with which you can drag and drop and change their order)
10. Navigate to the 'Deploy' tab, which is on the left side of the 'Settings' tab, in the deployment method section click on GitHub
11. To connect your GitHub code to Heroku, type in the name of your repository and then click on 'Search'. Once you see your repository show up click on 'Connect'
12. Choose a branch from which you wish to deploy.
13. You can choose to deploy your app manualy in the 'Manual Deploy' section click on 'Deploy Branch'
14. If you prefer you can also choose automatic deploys, in that case navigate to the 'Automatic Deploys' section and click on 'Enable Automatic Deploys', this method keeps the project up to date with your repository.

- Heroku requires two additional files for deployments
    
    - requirements.txt 
    - Profile

- To install the list of requirements which will go in your requirements.txt file you can use the following command:

    - `pip3 freeze > requirements.txt` 

- To create the Procfile you can use the following command:

    - `echo web: node index.js > Procfile`  

## Credits

### Code

- Some of the code is inspired by [Code Institute's](https://codeinstitute.net/) Love Sandwiches walkthrough project with some adjustments made.
- I used [this](https://pypi.org/project/colorama/) website to learn how to use Colorama.
- The display function and the main method are inspired by [this](https://www.youtube.com/watch?v=aEIHZDv_23U&ab_channel=ShaunHalverson) YouTube video.
- I chose the PyFiglet fonts from [here](http://www.figlet.org/examples.html)
- I learned how to use the PyFiglet library [here](https://pypi.org/project/pyfiglet/)
- I learned how to use the Datetime module [here](https://docs.python.org/3/library/datetime.html)
- I learned how to break long lines [here](https://peps.python.org/pep-0008/)
- [This](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc) YouTube playlist helped with concepts regarding the creation of the class 
- [This](https://www.geeksforgeeks.org/python-program-to-check-if-string-is-empty-or-not/) page of Geeks for Geeks' website helped me with the if statement using the .strip() method to check if the task that the user is trying to add is empty.
- The [gspread docs](https://docs.gspread.org/en/v5.1.0/index.html) website helped me with functions used to modify the spreadsheet. 

### Design 

- I used [Lucidchart](https://www.lucidchart.com/pages) to create the flowchart for the project.

### Acknowledgements

- I would like to acknowledge and thank the following people.

- Jubril Akolade - My Code Institute Mentor.
- The Code Institute Tutor Support - For their awesome and quick technical help.
- Thank you to everyone who took the time to use the app and give feedback.