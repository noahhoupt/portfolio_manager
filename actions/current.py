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

  live_prices = {}
  for ticker in tickers_list:
    live_prices[ticker] = si.get_live_price(ticker)

  live_value = {}
  live_portfolio_value = 0
  longest_ticker_symbol = get_longest_ticker_symbol(tickers_list)
  longest_value = get_longest_value(live_prices)
  print(longest_value)
  for row in buys_dataframe.itertuples():
    spaces_after_ticker = build_spaces_after_ticker(longest_ticker_symbol, row.ticker)
    spaces_after_value = build_spaces_after_value(longest_value, live_prices[row.ticker])
    ticker_equity = row.share_count * live_prices[row.ticker]
    live_value[row.ticker] = ticker_equity
    print_stock_info(row.ticker, spaces_after_ticker, live_prices[row.ticker], spaces_after_value, ticker_equity)
    live_portfolio_value = live_portfolio_value + ticker_equity

  print("Total Portfolio Value: " + str(round(live_portfolio_value,2)))


def print_stock_info(ticker, spaces_after_ticker, live_price, spaces_after_value, ticker_equity):
  stock_info_str = "Symbol: " + ticker + "   " + spaces_after_ticker \
    + "Value: " + str(round(live_price,2)) + "   " + spaces_after_value \
    + "Equity: " + str(round(ticker_equity,2))
  print(stock_info_str)


def get_owned_tickers_as_list(buys_dataframe):
  '''
  takes a dataframe and returns a string of ticker symbols
  that yfinance can digest
  '''
  tickers = []
  for row in buys_dataframe.ticker:
    tickers.append(row)
  return tickers


def get_longest_ticker_symbol(tickers_list):
  res = max(tickers_list, key = len)
  return len(res)


def build_spaces_after_ticker(longest_ticker_symbol, ticker):
  spaces_after_ticker =  longest_ticker_symbol - len(ticker)
  spaces = ""
  for i in range(spaces_after_ticker):
    spaces = spaces + " "
  return spaces


def get_longest_value(live_prices):
  max = -99
  for value in live_prices.values():
    digit_length = len(str(abs(round(value,2))))
    if max < digit_length:
      max = digit_length
  return max


def build_spaces_after_value(longest_live_prices, value):
  spaces_after_value = longest_live_prices - len(str(abs(round(value,2))))
  spaces = ""
  for i in range(spaces_after_value):
    spaces = spaces + " "
  return spaces
