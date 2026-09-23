# 🏠 Delhi House Price Prediction

A Machine Learning web application that predicts residential property prices in Delhi using Random Forest Regression.

## 📌 Project Overview

This project uses a dataset of 12,000+ Delhi property records to predict house prices based on property, location, and infrastructure features.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Google Colab

## 🤖 Machine Learning

Models compared:

- Linear Regression
- Random Forest Regression
- Gradient Boosting Regression

The Random Forest model achieved an R² score of approximately **0.913** on the test dataset.

### Evaluation

- MAE: ~₹37.3 lakh
- RMSE: ~₹75.5 lakh
- R²: ~0.913

## ⚙️ Features

The model uses features such as:

- District
- Locality
- Property Type
- Area
- Bedrooms
- Bathrooms
- Floor
- Furnishing
- Property Age
- Ownership Type
- Parking
- Balconies
- Nearby Metro, School and Hospital distances
- Road Width

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
