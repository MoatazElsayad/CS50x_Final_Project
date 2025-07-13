🪙 Currency Converter Dashboard
A full-stack web application built with Flask, HTML, CSS, and JavaScript that allows users to convert between currencies, track favorite conversions, and view real-time exchange rates using a third-party API.

* Features

- Real-time currency conversion
- Add and manage favorite currency pairs
- Conversion history for each user
- Fun random currency facts
- Export conversion history to CSV
- Responsive, user-friendly interface with flag icons and theme
- User authentication and secure session management

* Built With

- Python (Flask)
- HTML & CSS (Flexbox, Grid, Custom UI)
- JavaScript (DOM Manipulation, API calls)
- SQLite (via CS50 Library)
- Exchange Rate API (ExchangeRate-API)
- Jinja2 Templating

* Setup & Run Locally

1. Clone the repository:
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name

2. Install dependencies:
    pip install -r requirements.txt

3. Set environment variables (example for development):
    export FLASK_APP=app.py
    export FLASK_ENV=development

4. Run the app:
    flask run
