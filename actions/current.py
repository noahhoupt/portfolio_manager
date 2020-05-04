import yfinance as yf
from yahoo_fin import stock_info as si


def get_amount_invested(buys_dataframe):
  '''
  Takes a buys dataframe and returns the total amount
  invested (innacurate as avg_cost is rounded)
  '''
  accum = 0
  for row in buys_dataframe.itertuples():
    accum = accum + (row.avg_cost * row.share_count)

  amount_invested = accum
  print(amount_invested)
  return amount_invested


def get_portfolio_value(buys_dataframe):
  '''
  Takes a buys dataframe and returns the current total
  value of portfolio
  '''
  tickers_list = get_owned_tickers_as_list(buys_dataframe)

  live_price = {}
  for ticker in tickers_list:
    live_price[ticker] = si.get_live_price(ticker)
    print(ticker + ": " + str(si.get_live_price(ticker)))

  value = 0
  for row in buys_dataframe.itertuples():
    value = value + (row.share_count * live_price[row.ticker])

  print(value)



def get_owned_tickers_as_list(buys_dataframe):
  '''
  takes a dataframe and returns a string of ticker symbols
  that yfinance can digest
  '''
  tickers = []
  for row in buys_dataframe.ticker:
    tickers.append(row)
  return tickers
