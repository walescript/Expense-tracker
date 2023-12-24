# Expense Tracker Project

This project provides a simple framework for managing financial expenses. It consists of two main classes: `Expense` and `ExpenseDatabase`. The `Expense` class represents individual transactions, while the `ExpenseDatabase` class manages a collection of expenses.

## How to Clone the Code

To clone this project from GitHub, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the directory where you want to clone the project.

3. Run the following command:

   ```bash
   git clone https://github.com/walescript/expense-tracker.git


## Usage

### Expense Class

The `Expense` class is designed to represent an individual financial expense. Each expense has the following attributes:

- **`id`**: A unique identifier generated using UUID4.
- **`title`**: A string representing the title or description of the expense.
- **`amount`**: A float representing the monetary value of the expense.
- **`created_at`**: A datetime object indicating the creation timestamp.
- **`updated_at`**: A datetime object indicating the last update timestamp.

#### Methods

- `__init__(self, title: str, amount: float) -> None`: Initializes the expense attributes.
- `update(self, title: str = None, amount: float = None) -> None`: Updates the title and/or amount of the expense.
- `to_dict(self) -> dict`: Returns a dictionary representation of the expense.

### ExpenseDatabase Class

The `ExpenseDatabase` class manages a collection of expenses using a simple list. It provides methods for adding, removing, and retrieving expenses.

#### Methods

- `__init__(self) -> None`: Initializes the expense list.
- `add_expense(self, expense) -> None`: Adds an expense to the database.
- `remove_expense(self, expense_id) -> None`: Removes an expense from the database.
- `get_expense_by_id(self, expense_id) -> dict`: Retrieves an expense by ID.
- `get_expense_by_title(self, expense_title) -> list`: Retrieves expenses by title and returns a list.
- `to_dict(self) -> list`: Returns a list of dictionaries representing expenses in the database.

## Example Usage

```python
from expense_tracker import Expense, ExpenseDatabase

# Create an expense
expense1 = Expense("Christmas Clothes", 50000.0)

# Create an expense database
database = ExpenseDatabase()

# Add the expense to the database
database.add_expense(expense1)

# Update the expense
expense1.update(amount=60000.0)

# Retrieve expenses by title
expenses_by_title = database.get_expense_by_title("Christmas Clothes")

# Remove an expense
database.remove_expense(expense1.id)
