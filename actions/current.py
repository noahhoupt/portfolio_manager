import pandas as pd

def read_buys():
  csv_relative_path = "../buys.csv"

  buys = pd.read_csv(csv_relative_path)

  for row in buys:
    print(row)

def print_portfolio_value():
  read_buys()



