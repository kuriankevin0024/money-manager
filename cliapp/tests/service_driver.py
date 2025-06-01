from persistence.db import initialize_db
from models.expense_model import ExpenseModel
from services.expense_service import ExpenseService


def main():
    expense_service: ExpenseService = ExpenseService()
    expense_data: ExpenseModel = ExpenseModel(description='breakfast', amount=120.0, category='food', account='cash')

    created_expense: ExpenseModel = expense_service.create(expense=expense_data)
    print(f'Created Expense: {created_expense.__dict__}')

    read_expense: ExpenseModel = expense_service.read(id=created_expense.id)
    print(f'Read Expense: {read_expense.__dict__}')

    read_expense.description = 'lunch'
    updated_expense: ExpenseModel = expense_service.update(expense=read_expense)
    print(f'Updated Expense: {updated_expense.__dict__}')

    all_expenses: list[ExpenseModel] = expense_service.search()
    print(f'All Expenses: {[e.__dict__ for e in all_expenses]}')

    cash_expenses: list[ExpenseModel] = expense_service.search(account='cash')
    print(f'Cash Expenses: {[e.__dict__ for e in cash_expenses]}')

    deleted: bool = expense_service.delete(id=updated_expense.id)
    print('Deleted:', deleted)


if __name__ == '__main__':
    initialize_db()
    main()
