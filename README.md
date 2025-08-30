# Farmer Income Prediction Project

## 📌 Project Overview

This project predicts farmer incomes using diverse agricultural and
environmental data. The goal is to support fair and accessible lending
in India by improving credit assessments with data-driven insights. The
model was deployed using **Flask** with a simple web-based front-end for
user interaction.

------------------------------------------------------------------------

## 🛠️ Key Features

-   **Data Collection**:
-   Path: data/farmer_data.xlsx is a data used to build the model
-   Data collected from company competition
    datasets.
-   **Data Processing**: Cleaned, transformed, and selected meaningful
    agricultural features (rainfall, groundwater thickness, soil type,
    land usage, and seasonal temperatures).
-   **Modeling**: Used **XGBoost Regressor** for income prediction,
    applied log transformation to stabilize variance, and evaluated with
    regression metrics.
-   **Deployment**: Built a **Flask web application** with HTML/CSS for
    front-end, allowing users to input agricultural details and receive
    predictions in real-time.
-   **Output Formatting**: Predictions displayed in user-friendly format
    (Lakhs / Crores in Indian currency style).

------------------------------------------------------------------------

## 🚀 Tech Stack

-   **Languages**: Python, HTML, CSS
-   **Libraries**: Pandas, NumPy, Scikit-learn, XGBoost, Joblib
-   **Framework**: Flask
-   **Deployment**: Local Flask Server

------------------------------------------------------------------------

## 📊 Workflow

1.  Data Collection (company competition datasets).
2.  Data Cleaning and Feature Engineering.
3.  Model Training (XGBoost with feature selection).
4.  Web Application Development (Flask + HTML).
5.  Deployment and Testing.

------------------------------------------------------------------------

## 💻 How to Run

1.  Clone the repository.

2.  Install dependencies:

    ``` bash
    pip install -r requirements.txt
    ```

3.  Run Flask app:

    ``` bash
    python flask_app.py
    ```

4.  Open in browser:

        http://127.0.0.1:5000/

------------------------------------------------------------------------

## 📈 Future Improvements

-   Add interactive data visualizations for farmers.
-   Enhance dataset with real-time weather/market prices.
-   Deploy on cloud (AWS/GCP/Heroku) for public access.
-   Add multi-language support for accessibility.

------------------------------------------------------------------------

## 👨‍💻 Author

**Hithendra K S**\
MCA Student \| Data Analytics & Machine Learning Enthusiast
# Farmer-Project-Upload
