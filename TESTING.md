# Validation

I imported [this](https://pypi.org/project/pep8/) python style checker.

I used the [CI Python Linter](https://pep8ci.herokuapp.com/) to validate the code. After removing some blank lines, whitespaces and adjusting lines that were too long the code passed the validation with no issues.

![CI Python Linter Validation](https://github.com/devnickocodes/to-do-list-project/blob/main/documentation/pep8-validator.png)


## Manual Testing

|   Feature     |   Action                      |   Expected Result            |     PASS/FAIL     |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Program Start | N/A | Intro and Author texts shown, menu is displayed and user is prompted to choose one of the options | PASS |
| Menu          | Option 1 (Add Task) chosen | User is prompted to type in a task to be added to the list | PASS |
| Menu Option 1 (Add Task) | Types in a task to be added to the list | Task added to the list | PASS |
| Menu Option 1 (Add Task) | Tried to add an empty task | Error message displayed and user navigated to the menu | PASS |
| Menu          | Option 2 (View Tasks) chosen | (If there are tasks) Tasks with the statuses and timestamps are displayed | PASS |
| Menu          | Option 2 (View Tasks) chosen | (If there are no tasks) Display a message saying there are no tasks | PASS |





