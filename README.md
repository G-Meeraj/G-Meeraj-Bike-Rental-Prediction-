# 🚲 Bike Rental Prediction Web App

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-orange)
![License](https://img.shields.io/badge/License-MIT-green)

This is a Flask-based web application that predicts bike rental demand based on user-input environmental and seasonal parameters. The models are trained on historical data to make accurate rental forecasts.

---

## 🔍 Features

- Predict **daily** and **hourly** bike rental demand
- Interactive web interface using **Flask + HTML/CSS**
- Pre-trained machine learning models
- Simple and clean UI for user input

---

## 🏗️ Tech Stack

- Python 3.8+
- Flask
- Scikit-learn
- Pandas
- HTML, CSS (Jinja2 templates)

---

## 📦 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/G-Meeraj/bike-rental-prediction.git
cd bike-rental-prediction
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📥 Download Model Files

Due to GitHub's 100MB file limit, large model files are stored externally.

📌 **Download the following models manually** and place them in the `models/` directory:

- [Download `rf_hour_model.pkl`](https://drive.google.com/drive/folders/1JQNqyEfxG6YBTa1q8qghZ1ZXmH1dnfWt?usp=drive_link)
- [Download `daily_model.pkl`](https://drive.google.com/drive/folders/1JQNqyEfxG6YBTa1q8qghZ1ZXmH1dnfWt?usp=drive_link)

After downloading, ensure your directory looks like this:

```
bike-rental-prediction/
└── models/
    ├── rf_hour_model.pkl
    └── rf_hour_model.pkl
```

---

## 🚀 Run the App

```bash
flask run
```

Open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📁 Project Structure

```
bike-rental-prediction/
├── app.py
├── templates/
│   └── index.html
├── rf_hour_model.pkl
├──  daily_model.pkl
├── requirements.txt
└── README.md
```

---

## 📊 Example Inputs

- **Season**: 1 (Spring), 2 (Summer), 3 (Fall), 4 (Winter)
- **Working Day**: 0 (No), 1 (Yes)
- **Weather**: 1 (Clear), 2 (Mist), 3 (Rain/Snow)
- **Temperature & Humidity**: Normalized (0–1)

---

## 📃 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

Made with ❤️ by Meeraj 
[GitHub](https://github.com/G-Meeraj) • [LinkedIn](https://www.linkedin.com/in/your-profile)
