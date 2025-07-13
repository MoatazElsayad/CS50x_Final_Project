import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required, convert_currency, currency_wiki
from info import CURRENCY_INFO, MOST_TRADED_PAIRS, CURRENCY_FACTS
import datetime
import random

## For Export function ##
import csv
from io import StringIO
from flask import Response


app = Flask(__name__)
app.secret_key = "supersecretkey"

db = SQL("sqlite:///data.db")


# Index route for index.html
@app.route("/", methods=["GET", "POST"])
def index():
    from_currency = to_currency = amount = None
    result = None
    conversion_table = []
    reverse_table = []
    is_favorite = False
    currencies_wiki = {}
    preset_amounts = [10, 50, 100, 500, 1000, 5000]

    # If the method is POST, take the values from the form. Else, take it from the url.
    if request.method == "POST":
        from_currency = request.form.get("from_currency")
        to_currency = request.form.get("to_currency")
        amount = request.form.get("amount")
    else:
        from_currency = request.args.get("from")
        to_currency = request.args.get("to")
        amount = request.args.get("amount", 1)

    # If the form sent successfully and the inputs have values, do the functions below.
    if from_currency and to_currency and amount:
        # The amount has to be a float, otherwise return an error message.
        try:
            amount = float(amount)
        except ValueError:
            return render_template("index.html", error="Amount must be a number.", currency_info=CURRENCY_INFO)

        # take the result amount, the rate, and the reverse rate from the helpers.py function "convert_currency"
        result = convert_currency(from_currency, to_currency, amount)
        rate_info = convert_currency(from_currency, to_currency, 1)
        reverse_rate_info = convert_currency(to_currency, from_currency, 1)

        ## Functions for the common conversions table ##

        # If there is a rate info, return a dict with the amounts and their conversion rates.
        if rate_info:
            for amt in preset_amounts:
                conversion_table.append({
                    "amount": amt,
                    "converted": round(rate_info["rate"] * amt, 5)
                })

        # Reverse the process for the other table
        if reverse_rate_info:
            for amt in preset_amounts:
                reverse_table.append({
                    "amount": amt,
                    "converted": round(reverse_rate_info["rate"] * amt, 5)
                })

        # Check if the user is logged in and if there is a result.
        if result and "user_id" in session:
            # Insert the conversion into its table to display it in the history
            db.execute(
                "INSERT INTO conversions (user_id, from_currency, to_currency, amount, result, rate, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?)",
                session["user_id"], from_currency, to_currency, amount, result["converted_amount"], result["rate"], datetime.datetime.now()
            )

            # Get the favorites pair from the data base
            fav = db.execute(
                "SELECT 1 FROM favorites WHERE user_id = ? AND from_currency = ? AND to_currency = ?",
                session["user_id"], from_currency, to_currency
            )
            is_favorite = len(fav) > 0

        # Generate the wikipedia links for the pair of the currencies.
        if result:
            currencies_wiki = {
                "from": currency_wiki(CURRENCY_INFO[from_currency]["currency"]),
                "to": currency_wiki(CURRENCY_INFO[to_currency]["currency"])
            }

            # render the index.html and return the data used in the file.
            return render_template(
                "index.html", result=result, amount=amount,
                from_currency=from_currency, to_currency=to_currency,
                conversion_table=conversion_table,
                reverse_table=reverse_table,
                is_favorite=is_favorite,
                currency_info=CURRENCY_INFO,
                most_traded=MOST_TRADED_PAIRS,
                currencies_wiki=currencies_wiki
            )

        return render_template("index.html", error="Conversion failed. Please try again.", currency_info=CURRENCY_INFO, most_traded=MOST_TRADED_PAIRS)

    # If no form or query parameters submitted
    return render_template("index.html", currency_info=CURRENCY_INFO, most_traded=MOST_TRADED_PAIRS)


# Dashboard route for dashboard.html.
@app.route("/dashboard")
@login_required
def dashboard():
    user_id = session["user_id"]

    # Get the favorite conversion currency pairs
    favorites = db.execute(
        "SELECT from_currency, to_currency FROM favorites WHERE user_id = ?",
        user_id
    )

    # For each favorite, try to get the latest rate from the conversions table
    for pair in favorites:
         latest = db.execute(
             """
             SELECT rate FROM conversions
             WHERE from_currency = ? AND to_currency = ?
             ORDER BY timestamp DESC LIMIT 1
             """,
             pair["from_currency"], pair["to_currency"]
         )

         pair["rate"] = round(latest[0]["rate"], 5) if latest else "N/A"

    # Get latest 10 conversions
    history = db.execute(
        "SELECT * FROM conversions WHERE user_id = ? ORDER BY timestamp DESC LIMIT 10",
        user_id
    )

    # Choose a random fact to display on the dashboard
    random_fact = random.choice(CURRENCY_FACTS)

    return render_template("dashboard.html",
                            history=history, favorites=favorites,
                            currency_info=CURRENCY_INFO, random_fact=random_fact,
                            use_container=False
                            )

# Register route for register.html
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Get register data from the form
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Validate input
        if not username or not password or not confirmation:
            return render_template("register.html", error="All fields are required.")
        if password != confirmation:
            return render_template("register.html", error="Passwords do not match.")

        # Hash password
        hash_pw = generate_password_hash(password)

        # Try to insert the new user
        try:
            db.execute(
                "INSERT INTO users (username, hash) VALUES(?, ?)",
                username,
                hash_pw
            )
        except ValueError:
            return render_template("register.html", error="Username Already Exists!")

        # Log the user in (get their new id)
        rows = db.execute("SELECT id FROM users WHERE username = ?", username)
        session["user_id"] = rows[0]["id"]
        session["username"] = username

        flash("Registered successfully!")
        return redirect("/")

    return render_template("register.html")


# Login route for login.html
@app.route("/login", methods=["GET", "POST"])
def login():
    """ log user in """

    session.clear()

    if request.method == "POST":
        # Get login data from the form
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return render_template("login.html", error="All fields are required.")

        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return render_template("login.html", error="Invalid username and/or password.")

        session["user_id"] = rows[0]["id"]
        session["username"] = rows[0]["username"]

        flash("Logged In Successfully!")
        return redirect("/")

    return render_template("login.html")


# about me route for about-us.html
@app.route("/about-us")
def about_us():
    return render_template("about-us.html")


# about mb website route for about-mb.html
@app.route("/about-mb")
def about_mb():
    return render_template("about-mb.html")


# Favorite route for dashboard.html
@app.route("/favorite", methods=["POST"])
@login_required
def favorites():
    """Add a currency pair to the user's favorites."""
    data = request.get_json()
    from_cur = data.get("from_currency", "").upper()
    to_cur = data.get("to_currency", "").upper()

    # Gyard-clauses
    if not from_cur or not to_cur:
        return {"success": False, "error": "Missing currency pair."}, 400

    user_id = session["user_id"]

    # Check if favorite alrrady exists
    existing = db.execute(
        "SELECT 1 FROM favorites WHERE user_id = ? AND from_currency = ? AND to_currency = ?",
        user_id, from_cur, to_cur
    )

    # Delete the fav pairs if existed, insert it if not.
    if existing:
        db.execute(
            "DELETE FROM favorites WHERE user_id = ? AND from_currency = ? AND to_currency = ?",
            user_id, from_cur, to_cur
        )
        return {"success": True, "removed": True}
    else:
        db.execute(
            "INSERT INTO favorites (user_id, from_currency, to_currency) VALUES (?, ?, ?)",
            user_id, from_cur, to_cur
        )
        return {"success": True, "added": True}


# logout route to redirect to index.html the main page
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# delete route: redirect to register.html
@app.route("/delete", methods=["GET", "POST"])
@login_required
def delete():
    """Delete Account and All Related Data"""
    user_id = session["user_id"]

    if request.method == "POST":
        # Delete related data first (foreign keys may require this order)
        db.execute("DELETE FROM favorites WHERE user_id = ?", user_id)
        db.execute("DELETE FROM conversions WHERE user_id = ?", user_id)
        db.execute("DELETE FROM users WHERE id = ?", user_id)

        # Clear session
        session.clear()

        flash("Your account and all related data have been permanently deleted.")
        return redirect("/register")

    return render_template("delete.html")


# Export csv file route: existed in dashboard.html
@app.route("/export")
@login_required
def export():
    """Export conversion history as CSV"""
    user_id = session["user_id"]

    # Get user conversion history
    conversions = db.execute(
        "SELECT from_currency, to_currency, amount, result, rate, timestamp FROM conversions WHERE user_id = ? ORDER BY timestamp DESC",
        user_id
    )

    # Prepare CSV in memory
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["From", "To", "Amount", "Converted", "Rate", "Date/Time"])

    # write the csv file
    for c in conversions:
        writer.writerow([
            c["from_currency"],
            c["to_currency"],
            c["amount"],
            c["result"],
            c["rate"],
            c["timestamp"]
        ])

    # return the cursor to the first character to write over the last csv.
    output.seek(0)

    # Select the username to put it in csv file's name.
    username = db.execute("SELECT username FROM users WHERE id = ?", user_id)[0]["username"]
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": f"attachment; filename={username}-conversions.csv"}
    )


### End of app.py ###
