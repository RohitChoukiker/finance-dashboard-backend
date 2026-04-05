from enum import Enum

class TransactionCategory(str, Enum):

    salary = "salary"
    food = "food"
    travel = "travel"
    shopping = "shopping"
    rent = "rent"
    bills = "bills"
    health = "health"
    entertainment = "entertainment"