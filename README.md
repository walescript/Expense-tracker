This project provides a basic framework for managing financial expenses. It includes two main classes: Expense and ExpenseDatabase. The Expense class represents individual financial transactions, while the ExpenseDatabase class manages a collection of expenses.

Usage
Expense Class
The Expense class is designed to represent an individual financial expense. Each expense has the following attributes:

id: A unique identifier generated using UUID4.
title: A string representing the title or description of the expense.
amount: A float representing the monetary value of the expense.
created_at: A datetime object indicating the creation timestamp.
updated_at: A datetime object indicating the last update timestamp.
Methods
__init__(self, title: str, amount: float) -> None: Initializes the expense attributes.
update(self, title: str = None, amount: float = None) -> None: Updates the title and/or amount of the expense.
to_dict(self) -> dict: Returns a dictionary representation of the expense.

ExpenseDatabase Class
The ExpenseDatabase class manages a collection of expenses using a simple list. It provides methods for adding, removing, and retrieving expenses.

Methods
__init__(self) -> None: Initializes the expense list.
add_expense(self, expense) -> None: Adds an expense to the database.
remove_expense(self, expense_id) -> None: Removes an expense from the database.
get_expense_by_id(self, expense_id) -> dict: Retrieves an expense by ID.
get_expense_by_title(self, expense_title) -> list: Retrieves expenses by title and returns a list.
to_dict(self) -> list: Returns a list of dictionaries representing expenses in the database.
