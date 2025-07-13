import requests

from cs50 import SQL
from functools import wraps
from flask import redirect, session
import datetime

db = SQL("sqlite:///data.db")

# My API url.
API_KEY = "552293161ef031ac47e9d93f"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest"


# A decorated function to check that the user should be logged in before using specific routes
def login_required(f):
    """
    Decorator to require login for specific routes.
    Usage: @login_required above any Flask route.
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


# Function that deals with the conversion process
def convert_currency(from_currency, to_currency, amount):
    """
    Convert amount from one currency to another using ExchangeRate-API v6,
    checking for recent history first
    """

    # 1. Check if we have a recent rate already stored (regardless of amount)
    now = datetime.datetime.now()
    hour_ago = now - datetime.timedelta(minutes=60)

    recent = db.execute(
        """
        SELECT rate FROM conversions
        WHERE from_currency = ? AND to_currency = ?
        AND timestamp >= ?
        ORDER BY timestamp DESC LIMIT 1
        """,
        from_currency, to_currency, hour_ago
    )

    if recent:
        rate = recent[0]["rate"]
        converted_amount = round(rate * amount, 5)
        print("api is not used")
    else:
        # 2. Otherwise, call the API
        try:
            # Get all rates from the base currency
            url = f"{BASE_URL}/{from_currency}"
            response = requests.get(url)
            data = response.json()

            if data["result"] != "success":
                return None

            # Get exchange rate to target currency
            rate = data["conversion_rates"].get(to_currency)
            if rate is None:
                return None

            # Get the converted amount rounded to 5 decimals
            converted_amount = round(rate * amount, 5)

            # 3. Store new result in database (regardless of user)
            db.execute(
                """
                INSERT INTO conversions (user_id, from_currency, to_currency, amount, result, rate, timestamp)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                session.get("user_id"), from_currency, to_currency, amount, converted_amount, rate, now
            )
            print("api is used")
        except Exception as e:
            print("API error:", e)
            return None
    # 4. Save current user's request to track their activity
    if session.get("user_id"):
        db.execute(
            """
            INSERT INTO conversions (user_id, from_currency, to_currency, amount, result, rate, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            session["user_id"], from_currency, to_currency, amount, converted_amount, rate, now
        )

    return {
        "converted_amount": converted_amount,
        "rate": round(rate, 5),
        "from": from_currency,
        "to": to_currency,
        "source": "cache" if recent else "api"
    }


# Function that returns wikipidia links for the currency pair.
def currency_wiki(currency):
    """Generate Wikipedia's link for a selected currency"""

    curr_route = currency.replace(" ", "_")

    return f"https://en.wikipedia.org/wiki/{curr_route}"

### End of helpers.py ###
