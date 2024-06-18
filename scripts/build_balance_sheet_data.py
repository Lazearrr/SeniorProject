from dotenv import load_dotenv
import requests
import os
import re
import mysql.connector

load_dotenv()
AV_APIKEY = os.environ.get('AV_APIKEY')

# Initialize MySQL connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lowdog541.",
    database="valueinvestor"
)

cursor = mydb.cursor()

# SQL insert query template
sql = "INSERT INTO your_table (ticker, json_data) VALUES (%s, %s)"

with open('./nyse_all_listed.txt', 'r') as file:
    lines = file.readlines()

tickers = []
pattern = re.compile(r'^([A-Z$]+),')

for line in lines:
    match = pattern.match(line)
    if match:
        tickers.append(match.group(1))

for ticker in tickers:
    url = f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={ticker}&apikey={AV_APIKEY}'
    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()
        val = (ticker, str(json_data))
        cursor.execute(sql, val)
        
        print(f"Data for {ticker} inserted.")
    else:
        print(f"Failed to get data for {ticker}")

mydb.commit()
cursor.close()
mydb.close()