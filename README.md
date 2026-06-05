# 🚗 Pick My Car — Used Car Price Estimator

A machine learning web application that predicts the resale price of used cars based on vehicle details. Built with Flask and a Linear Regression model trained on real-world car listings data.

---

## 🔍 Overview

**Pick My Car** allows users to enter details about a used car — manufacturer, model, year, fuel type, and kilometres driven — and instantly receive an estimated resale price powered by a trained ML model.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| ML Model | Scikit-learn (Linear Regression) |
| Data Processing | Pandas, NumPy |
| Frontend | HTML, CSS, Vanilla JavaScript |
| Deployment | Render |

---

## 📁 Project Structure

```
pick-my-car/
│
├── app.py                      # Flask application & routes
├── LinearRegressionModel.pkl   # Trained ML model
├── Cleaned_car.csv             # Preprocessed dataset
├── requirements.txt            # Python dependencies
│
├── templates/
│   └── index.html              # Main UI template (Jinja2)
│
└── static/
    └── css/
        └── style.css           # Stylesheet
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/ayush-130904/price_my_car.git
cd pick-my-car
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## 📦 Requirements

```
flask
flask-cors
pandas
numpy
scikit-learn
gunicorn
```

---

## 🤖 How It Works

1. The dataset (`Cleaned_car.csv`) is loaded on startup to populate dropdown options (manufacturer, car model, year, fuel type).
2. User fills in the form with vehicle details.
3. On submission, the form data is sent via `POST` to `/predict`.
4. The trained `LinearRegressionModel.pkl` predicts the resale price.
5. The estimated price is returned and displayed in Indian Rupees (₹).

---

## 🚀 Deployment (Render)

This app is deployed on [Render](https://price-my-car.onrender.com).

**Start command used:**
```
gunicorn app:app
```

> **Note:** The app is hosted on Render's free tier. It may take **30–50 seconds** to load after a period of inactivity due to cold starts.

---

## 📊 Dataset

- Source: Scrapped Data from Quikr.com, listing cars required information(`quikr.csv`)
- Preprocessed into `Cleaned_car.csv` — missing values removed, data types corrected, outliers handled.
- Features used: `car_name`, `company_name`, `year`, `kms_driven`, `fuel_type`
- Target: `Price` (in INR)

---

## 📸 Preview

<img width="1886" height="992" alt="Screenshot (91)" src="https://github.com/user-attachments/assets/c4ba8271-25f2-4444-a4e0-3f743ed4a94a" />



---

## 👤 Author

**Ayush**  
Mumbai University — Engineering Student  
Applied Data Science Project

---

## 📄 License

This project is for academic purposes only.
