import sys
import os
from fastapi.testclient import TestClient

# Add the parent directory to sys.path to allow importing app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app

client = TestClient(app)

def test_finance_domain():
    print("Testing Finance Domain APIs...")

    # 1. Expense Type
    response = client.post("/finance/expense_types/", json={
        "name": "Tuition Fee",
        "description": "Cost for instruction"
    })
    assert response.status_code == 200
    expense_id = response.json()["expense_type_id"]
    print(f"Expense Type Created: {expense_id}")

    # 2. Financial Aid Type
    response = client.post("/finance/financial_aid_types/", json={
        "name": "Merit Scholarship",
        "description": "Based on academic performance"
    })
    assert response.status_code == 200
    aid_id = response.json()["financial_aid_type_id"]
    print(f"Financial Aid Type Created: {aid_id}")

    # 3. Currency
    response = client.post("/finance/currencies/", json={
        "name": "Indian Rupee",
        "currency_code": "INR"
    })
    assert response.status_code == 200
    currency_id = response.json()["currency_id"]
    print(f"Currency Created: {currency_id}")

    # Cleanup
    client.delete(f"/finance/currencies/{currency_id}")
    client.delete(f"/finance/financial_aid_types/{aid_id}")
    client.delete(f"/finance/expense_types/{expense_id}")
    print("Cleanup Complete.")

if __name__ == "__main__":
    try:
        test_finance_domain()
        print("All Finance Domain tests passed successfully.")
    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)
