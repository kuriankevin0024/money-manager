from datetime import date
import tools.tools as tools

def test_simple_interest_projection():
    start_date: date = date(year=2025, month=1, day=15)
    simple_interest_projection: dict = tools.simple_interest_projection(
        starting_balance=10_000.00, interest_rate=8.00, start_date=start_date, years=3)
    assert simple_interest_projection.get('interest_accrued') == 2400.00
    assert simple_interest_projection.get('final_balance') == 12400.00
    assert simple_interest_projection.get('monthly_interest') == 66.67
    assert simple_interest_projection.get('end_date') == date(year=2028, month=1, day=15)
    print()
    print(f"initial_balance: {simple_interest_projection.get('initial_balance')}")
    print(f"interest_accrued: {simple_interest_projection.get('interest_accrued')}")
    print(f"final_balance: {simple_interest_projection.get('final_balance')}")
    print(f"monthly_interest: {simple_interest_projection.get('monthly_interest')}")
    print(f"end_date: {simple_interest_projection.get('end_date').strftime('%B %Y')}")
