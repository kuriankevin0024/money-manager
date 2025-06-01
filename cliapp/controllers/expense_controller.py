import uvicorn
from datetime import date
from typing import Optional, Any
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Query, status, Response

from persistence.db import initialize_db
from services.expense_service import ExpenseService
from models.expense_model import ExpenseModel, ExpenseSchema

application = FastAPI()
expense_service = ExpenseService()


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f'Uvicorn server is starting up...')
    initialize_db()
    yield
    print(f'Uvicorn server shutdown completed.')


application.router.lifespan_context = lifespan


@application.post('/expenses', response_model=ExpenseSchema)
def create(payload: ExpenseSchema) -> ExpenseSchema:
    input_data: dict[str, Any] = payload.model_dump(exclude={'id'})
    input_expense: ExpenseModel = ExpenseModel(**input_data)
    created_expense: ExpenseModel = expense_service.create(expense=input_expense)
    return created_expense


@application.get('/expenses/{expense_id}', response_model=ExpenseSchema)
def read(expense_id: int) -> ExpenseSchema:
    read_expense: ExpenseModel = expense_service.read(id=expense_id)
    if not read_expense:
        raise HTTPException(status_code=404, detail='Expense not found')
    return read_expense


@application.put('/expenses/{expense_id}', response_model=ExpenseSchema)
def update_expense(expense_id: int, payload: ExpenseSchema) -> ExpenseSchema:
    read_expense: ExpenseModel = expense_service.read(id=expense_id)
    if not read_expense:
        raise HTTPException(status_code=404, detail='Expense not found')

    read_expense.description = payload.description
    read_expense.amount = payload.amount
    read_expense.category = payload.category
    read_expense.account = payload.account

    updated_expense: ExpenseModel = expense_service.update(expense=read_expense)
    return updated_expense


@application.delete("/expenses/{expense_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_expense(expense_id: int) -> Response:
    read_expense: ExpenseModel = expense_service.read(id=expense_id)
    if not read_expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    deleted = expense_service.delete(id=expense_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Failed to delete expense")

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@application.get("/expenses", response_model=list[ExpenseSchema])
def search_expenses(
        category: Optional[str] = Query(None),
        account: Optional[str] = Query(None),
        date_from: Optional[date] = Query(None),
        date_to: Optional[date] = Query(None)
) -> list[ExpenseSchema]:
    results = expense_service.search(
        category=category,
        account=account,
        date_from=date_from,
        date_to=date_to
    )
    return results


if __name__ == '__main__':
    initialize_db()
    uvicorn.run('cliapp.controllers.expense_controller:application', host='127.0.0.1', port=8000, reload=True)
