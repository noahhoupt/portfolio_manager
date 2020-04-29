import pandas as pd
import os.path

def read_buys():
  buys_csv_path = os.path.dirname(__file__) + '/../buys.csv'
  buys = pd.read_csv(buys_csv_path)

  print(buys)

def print_portfolio_value():
  read_buys()



