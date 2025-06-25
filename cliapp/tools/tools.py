from datetime import date
from dateutil.relativedelta import relativedelta


def future_date(start_date: date, years: int = 0, months: int = 0, weeks: int = 0, days: int = 0) -> date:
    return start_date + relativedelta(years=years, months=months, weeks=weeks, days=days)


def simple_interest(starting_balance: float, interest_rate: float, years: float) -> float:
    return starting_balance * (interest_rate / 100) * years


def simple_interest_projection(starting_balance: float, interest_rate: float, start_date: date, years: int) -> dict:
    interest_accrued: float = simple_interest(
        starting_balance=starting_balance, interest_rate=interest_rate, years=years)
    final_balance: float = starting_balance + interest_accrued
    monthly_interest: float = round(interest_accrued / (years * 12), 2)
    end_date: date = future_date(start_date=start_date, years=years)
    return {'initial_balance': starting_balance, 'interest_accrued': interest_accrued, 'final_balance': final_balance,
            'monthly_interest': monthly_interest, 'end_date': end_date}
