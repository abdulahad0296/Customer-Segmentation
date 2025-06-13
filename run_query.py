'''
Here we wil use SQL queries to answer the following questions:

    1. What is the distribution of order values across all customers in the dataset?

    2. How many unique products has each customer purchased?

    3. Which customers have only made a single purchase from the company?

    4. Which products are most commonly purchased together by customers in the dataset?
'''


import sqlite3
import pandas as pd

def run_query(query):
    conn = sqlite3.connect("customers.db")
    df=pd.read_sql_query(query,conn)
    conn.close()
    
    return df

queries={
    "Table Preview":"""
    SELECT * 
    FROM transactions
    LIMIT 30
    """,
    "1. Order Value Distribution":"""
    SELECT 
    CustomerID, ROUND(SUM(CAST(UnitPrice AS REAL)*Quantity), 2) AS TotalOrderValue 
    FROM transactions 
    GROUP BY CustomerID 
    ORDER BY TotalOrderValue DESC 
    LIMIT 10
    """,

    "2.Unique Products per Customer":"""
    SELECT 
    CustomerID, COUNT(DISTINCT StockCode) AS UniqueProduct 
    FROM transactions 
    GROUP BY CustomerID 
    ORDER BY UniqueProduct DESC 
    LIMIT 10
    """,

    "3.One-Time Customer":"""
    SELECT 
    CustomerID, COUNT(DISTINCT InvoiceNo) AS ProductCount 
    FROM transactions 
    GROUP BY CustomerID 
    HAVING ProductCount=1
    """,

    "4. Items Frequently Bought Together":"""
    SELECT 
        a.Description AS Product1, 
        b. Description AS Product2, 
    COUNT(*) AS BoughtTogether 
    FROM transactions a 
    JOIN transactions b 
        ON a.InvoiceNo = b.InvoiceNo 
        AND a.StockCode < b.StockCode 
    GROUP BY a.Description, b.Description 
    ORDER BY BoughtTogether DESC 
    LIMIT 10
    """
}