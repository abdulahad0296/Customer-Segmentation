# 🧠 Customer Segmentation Dashboard

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.35.0-orange)
![License](https://img.shields.io/badge/license-MIT-green)
![Last Commit](https://img.shields.io/github/last-commit/abdulahad0296/customer_segmentation)
![GitHub stars](https://img.shields.io/github/stars/abdulahad0296/customer_segmentation?style=social)

## 📋 Overview

A Streamlit app for customer segmentation using SQL queries on the Online Retail Dataset.

## 📁 Project Structure

customer_segmentation/
├── app.py # Main Streamlit UI\
├── customers.db # SQLite3 database\
├── load_data.py # One-time data cleaning and DB insertion\
├── OnlineRetail.csv # CSV file being processed\
├── README.md\ 
├── requirements.txt\
├── run_query.py # SQL query execution and logic\
└── test.ipynb # EDA notebook\ 


## 🔧 Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/abdulahad0296/customer_segmentation.git
cd customer_segmentation



2. (Optional but recommended) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. (Optional) Load the data into the database:

```bash
python load_data.py
```

5. Run the Streamlit app:

```bash
streamlit run app.py
```

## 📊 Features

* Preview Data Table
* View top-spending customers
* See which products are most frequently bought together
* Analyze one-time buyers vs repeat customers


## 📚 Dataset Source

* [Kaggle Online Retail Data Set](https://www.kaggle.com/datasets/vijayuv/onlineretail)
## 📌 Notes

* Cleaned rows with null `CustomerID` and filled missing `Description` values with `"Unknown Product"`.

## 🧑‍💻 Author

Abdul Ahad


