from uuid import uuid4
from datetime import datetime


class Expense:
    '''Represents an individual financial expense'''
    def __init__(self,title :str,amount : float) -> None:
        '''This method initializes the Expense attributes'''
        self.id = str(uuid4())
        self.title = str(title)
        self.amount = float(amount)
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def update(self, title: str = None, amount: float = None) -> None:
        '''This method updates the title and/or amount of the expense.'''
        if title:
            self.title = title
        if amount:
            self.amount = amount
        self.updated_at = datetime.utcnow()
        return f"title: {self.title}, amount: {self.amount} has been updated"


    def to_dict(self) -> dict:
        '''This method returns a dictionary representation of the expense.'''
        return dict(id=self.id,title=self.title,amount=self.amount,created_at=self.created_at,updated_at=self.updated_at)


class ExpenseDatabase:
    '''Manages a collection of Expense'''
    def __init__(self):
        '''This method initializes the expense list'''
        self.expenses = []

    def add_expense(self, expense):
        '''This method adds an expense to the database'''
        self.expenses.append(expense.to_dict())
        print('expense has been added successfully!')

    def remove_expense(self, expense_id):
        '''This method removes an expense from the database'''
        self.expenses = [unit_expense for unit_expense in self.expenses if unit_expense['id'] != expense_id]
        print(f"{expense_id} has been removed successfully!")
        
    def get_expense_by_id(self, expense_id):
        '''This method retrieves an expense by ID'''
        for expense in self.expenses:
            if expense['id'] == expense_id:
                return expense
        
    def get_expense_by_title(self, expense_title) -> list:
        '''This method retrieves an expense by title and returns a list'''
        return [unit_expense for unit_expense in self.expenses if unit_expense['title'] == expense_title]
        
    def to_dict(self):
        '''This method returns a list of dictionaries representing expenses in the DB'''
        return [expense.to_dict() for expense in self.expenses]