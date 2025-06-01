from datetime import date
from typing import Optional

from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from sqlalchemy.sql.dml import Update, Delete
from sqlalchemy import Select, select, update, delete

from persistence.db import SessionFactory
from models.expense_model import ExpenseModel


class ExpenseService:
    @staticmethod
    def create(expense: ExpenseModel) -> ExpenseModel:
        session: Session = SessionFactory()
        try:
            expense.created_date = date.today()
            session.add(expense)
            session.commit()
            session.refresh(expense)
            return expense
        finally:
            session.close()

    @staticmethod
    def read(id: int) -> ExpenseModel:
        session: Session = SessionFactory()
        try:
            return session.get(entity=ExpenseModel, ident=id)
        finally:
            session.close()

    @staticmethod
    def update(expense: ExpenseModel) -> ExpenseModel:
        session: Session = SessionFactory()
        try:
            statement: Update = (
                update(table=ExpenseModel)
                .where(ExpenseModel.id == expense.id)
                .values(
                    description=expense.description,
                    amount=expense.amount,
                    category=expense.category,
                    account=expense.account,
                    created_date=expense.created_date
                )
            )
            session.execute(statement=statement)
            session.commit()
            return ExpenseService.read(id=expense.id)
        finally:
            session.close()

    @staticmethod
    def delete(id: int) -> bool:
        session: Session = SessionFactory()
        try:
            statement: Delete = delete(table=ExpenseModel).where(ExpenseModel.id == id)
            result: Result = session.execute(statement=statement)
            session.commit()
            return result.rowcount == 1
        finally:
            session.close()

    @staticmethod
    def search(
            *,
            category: Optional[str] = None,
            account: Optional[str] = None,
            date_from: Optional[str] = None,
            date_to: Optional[str] = None
    ) -> list[ExpenseModel]:
        statement: Select = select(ExpenseModel)
        if category:
            statement: Select = statement.where(ExpenseModel.category == category)
        if account:
            statement: Select = statement.where(ExpenseModel.account == account)
        if date_from:
            statement: Select = statement.where(ExpenseModel.created_date >= date_from)
        if date_to:
            statement: Select = statement.where(ExpenseModel.created_date <= date_to)

        session: Session = SessionFactory()
        try:
            return session.execute(statement=statement).scalars().all()
        finally:
            session.close()
