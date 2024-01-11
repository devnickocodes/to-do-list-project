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

This feature allows the user to create a task that will be stored in Google Spreadsheet. It logs the task in the first cell, creates a status variable with an initial status of ‘Not Done’ and logs it in the second cell and finally creates a timestamp which is logged in the third cell of the spreadsheet. After that the user is directed to the menu again.

![Add Task (Option - 1)](https://github.com/devnickocodes/to-do-list-project/blob/main/documentation/add-a-task.png)

### View Tasks

This feature retrieves all the available tasks with their statuses and timestamps and displays them to the user. After that the user is directed to the menu again.

![View Tasks (Option - 2)](https://github.com/devnickocodes/to-do-list-project/blob/main/documentation/view-tasks.png)

### Remove Task

Next feature displays all the available tasks and takes a user input as to which task should be removed, if the task exists it is removed from the spreadsheet, if it doesn’t the user is directed to the menu again.

![Remove Task (Option - 3)](https://github.com/devnickocodes/to-do-list-project/blob/main/documentation/remove-task.png)

### Mark Task As Done 

This feature displays all the available tasks and takes a user input as to which task should be marked as done. If the task exists the second cell for that task in the spreadsheet, which is the status cell is updated to ‘Done’ after which the user is directed to the menu again.

![Mark Task As Done (Option - 4)](https://github.com/devnickocodes/to-do-list-project/blob/main/documentation/mark-task-as-done.png)

### Mark Task As Not Done

This feature displays all the available tasks and takes a user input as to which task should be marked as not done. If the task exists the second cell for that task in the spreadsheet, which is the status cell is updated to ‘Not Done’ after which the user is directed to the menu again.

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

- The project was developed using Python.
    - [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

- The script used to run the Code Institute mock terminal is done with JavaScript.
    - [JavaScript](https://en.wikipedia.org/wiki/JavaScript)



    