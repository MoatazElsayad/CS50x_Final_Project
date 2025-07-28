# MB Currency Converter

#### Video Demo: https://youtu.be/vLPi9Mm9WhM
#### Description:

MB Currency Converter is a full-stack web application that allows users to seamlessly convert between different currencies, view real-time exchange rates, manage a list of favorite currency pairs, and export their conversion history.

This project was created as my final submission for CS50x. It is built using **Flask (Python)** on the backend, **HTML**, **CSS**, and **JavaScript** on the frontend, and integrates an external **ExchangeRate-API** for up-to-date conversion data. Users can sign up, log in, perform conversions, save favorites, and view random currency facts for a more engaging experience.

The app features a clean and responsive user interface with flag icons and themes, making it both functional and visually appealing.

---

## ✨ Features

- 🔁 Real-time currency conversion via API
- ❤️ Add and manage favorite currency pairs
- 🕒 View full conversion history per user
- 📊 Export conversion history as CSV
- 🌍 Display of random currency facts
- 🌙 Responsive, themed interface with country flags
- 🔐 User authentication and secure session management

---

## 🛠️ Languages & Tools Used

- **Python** (Flask framework)
- **HTML** & **CSS** (Flexbox, Grid, custom responsive UI)
- **JavaScript** (DOM manipulation & API integration)
- **SQL** with **SQLite** (via CS50 Library)
- **JSON** (for API responses and local storage)
- **Jinja2** (for dynamic HTML rendering)
- **Git** (for version control)
- **ExchangeRate-API** (currency data source)

---

## 📁 Project Structure

- app.py: Main Flask application file
- templates/: Contains all Jinja2 HTML templates
- static/: CSS, JavaScript, images, and flag assets
- helpers.py: Custom helper functions
- requirements.txt: Python dependencies
- data.db: SQL for database
- README.md: Project documentation

---

## 🚀 How to Run Locally

1. **Clone the repository**
git clone https://github.com/MoatazElsayad/CS50x_Final_Project.git
cd CS50x_Final_Project

2. **Install dependencies**
pip install -r requirements.txt

3. **Set environment variables (example for development)**
export FLASK_APP=app.py
export FLASK_ENV=development

4. **Run the app**
flask run
Visit http://127.0.0.1:5000 in your browser.
