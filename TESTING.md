# Validation

I imported [this](https://pypi.org/project/pep8/) python style checker.

I used the [CI Python Linter](https://pep8ci.herokuapp.com/) to validate the code. After removing some blank lines, whitespaces and adjusting lines that were too long the code passed the validation with no issues.

![CI Python Linter Validation](https://github.com/devnickocodes/to-do-list-project/blob/main/documentation/pep8-validator.png)


## Manual Testing

|   Feature     |   Action                      |   Expected Result            |     PASS/FAIL     |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Program Start | N/A | Intro and Author texts shown, menu is displayed and user is prompted to choose one of the options | PASS |
| Menu          | Option 1 (Add Task) chosen | User is prompted to type in a task to be added to the list | PASS |
| Menu Option 1 (Add Task) | Types in a task to be added to the list | Task added to the list and user is navigated to the menu | PASS |
| Menu Option 1 (Add Task) | Tried to add an empty task | Error message displayed and user is navigated to the menu | PASS |
| Menu          | Option 2 (View Tasks) chosen | (If there are tasks) Tasks with the statuses and timestamps are displayed and user is navigated to the menu | PASS |
| Menu          | Option 2 (View Tasks) chosen | (If there are no tasks) Display a message saying there are no tasks and user is navigated to the menu| PASS |
| Menu          | Option 3 (Remove Task) chosen | (If there are no tasks) Display a message saying there are no tasks and user is navigated to the menu| PASS |
| Menu          | Option 3 (Remove Task) chosen | (If there are tasks) Prompt the user to input the number of the task they want to remove | PASS |
| Menu Option 3 (Remove Task) chosen | The user chooses a task number that matches one of the tasks | Task is removed and user is navigated to the menu| PASS |
| Menu Option 3 (Remove Task) chosen | The user chooses a task number that does not match one of the tasks | Display invalid task number and user is navigated to the menu | PASS |
| Menu Option 3 (Remove Task) chosen | The user inputs a letter | Display an error message and user is navigated to the menu | PASS |
| Menu Option 3 (Remove Task) chosen | The user inputs an empty input | Display an error message and user is navigated to the menu | PASS |
| Menu          | Option 4 (Mark Task As Done) chosen | (If there are no tasks) Display a message saying there are no tasks and user is navigated to the menu| PASS |
| Menu          | Option 4 (Mark Task As Done) chosen | (If there are tasks) Prompt the user to input the number of the task they want to mark as done | PASS |
| Menu Option 4 (Mark Task As Done) chosen | The user chooses a task number that matches one of the tasks | Task is marked as done and user is navigated to the menu | PASS |
| Menu Option 4 (Mark Task As Done) chosen | The user chooses a task number that does not match one of the tasks | Display invalid task number and user is navigated to the menu | PASS |
| Menu Option 4 (Mark Task As Done) chosen | The user inputs a letter | Display an error message and user is navigated to the menu | PASS |
| Menu Option 4 (Mark Task As Done) chosen | The user inputs an empty input | Display an error message and user is navigated to the menu | PASS |
| Menu          | Option 5 (Mark Task As Not Done) chosen | (If there are no tasks) Display a message saying there are no tasks and user is navigated to the menu | PASS |
| Menu          | Option 5 (Mark Task As Not Done) chosen | (If there are tasks) Prompt the user to input the number of the task they want to mark as not done | PASS |
| Menu Option 5 (Mark Task As Not Done) chosen | The user chooses a task number that matches one of the tasks | Task is marked as not done and user is navigated to the menu | PASS |
| Menu Option 5 (Mark Task As Not Done) chosen | The user chooses a task number that does not match one of the tasks | Display invalid task number and user is navigated to the menu | PASS |
| Menu Option 5 (Mark Task As Not Done) chosen | The user inputs a letter | Display an error message and user is navigated to the menu | PASS |
| Menu Option 5 (Mark Task As Not Done) chosen | The user inputs an empty input | Display an error message and user is navigated to the menu | PASS |