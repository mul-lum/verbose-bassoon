# verbose-bassoon
Collaborative Project by Jaycob and Muneeb

## 📌 Introduction
This project is a Python-based Expense Tracker that allows users to add, view, filter, calculate, and delete expenses. The program uses **Python dictionaries** to store expense data such as category, amount, and date. The project was developed collaboratively using GitHub.

## 🔧 Usage
Download from `releases`, and follow instructions from there...

> Download `expense_tracker.py` in `main` branch, then run `python3 expense_tracker.py` (based on python installation) in terminal. 

## ⚙️ Features   
- Add new expenses (category, amount, date)
- View all recorded expenses
- Filter expenses by category
- Calculate total expenses
- Delete expenses by ID
- Error handling for invalid inputs
- Clear, modular, and well-commented code

### ➕ *Add/Categorizing Expenses*
Adding expenses and categorizing them is simple within our program. All in one command, using `add [name] [amount] [category]`... Category is optional and if no category parameter is passed than will default to None

### ➖ *Removing Expenses/Categories*
Removing categories or expenses is crucial for managing expenses and accuracy of the budgetting. `remove [context]`, context could either be a category name or expense name.

### 🔍 *Viewing Expenses/Categories*
Viewing a certain category of expenses or a singular expense is done easy and simple for all users. `view [ctx]`.

### 💯 *Viewing the Total of a Category*
Knowing the total of a certain category of expenses is important when you want to save money. Using `sum [category]` will calculate the total of the category and return it in a readable fashion.

## ⭐ Credits

* Jaycob
 (Lead Developer)
> Designed and implemented the core Python program

> Developed main features including adding, viewing, calculating, filtering, and deleting expenses

> Handled error checking, code structure, and overall logic

> Taught other groupmate on how to improve ReadMe

* Muneeb
 > Wrote and organized the README file

 > Documented project features, instructions, and reflection

 > Assisted with reviewing code and coordinating GitHub submissions

 > Helped with code

## 💭 Reflection

### Challenges Faced

- Managing merge conflicts when multiple members edited the same file

- Ensuring consistent variable naming across branches

- Handling invalid user input without crashing the program

### How We Overcame Them

- Used separate Git branches for each feature

- Reviewed pull requests carefully before merging

- Added try-except blocks for error handling

### Collaborative Coding Experience

We enjoyed collaborative coding because it allowed us to divide tasks efficiently and learn from each other. It was a new exprince and GitHub helped us collaboratie better and track changes clearly.
