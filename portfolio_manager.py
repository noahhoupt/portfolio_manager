import argparse
import os.path
import pandas as pd
from actions.current import get_portfolio_value, get_amount_invested

def get_parser():
  parser = argparse.ArgumentParser(
    description="It tracks statistics related to your stock portfolio in real time"
  )
  parser.add_argument(
    "-c",
    "--current",
    action='store_true',
    default=False,
    help="Prints current value of portfolio"
  )
  parser.add_argument(
    "-r",
    "--report",
    action='store_true',
    default=False,
    help="Stores value of current portfolio in report.txt file"
  )
  return parser


def get_arg_values(args):
  args_vals = []
  for key in args.__dict__:
    args_vals.append(args.__dict__[key])
  return args_vals


def get_buys_dataframe():
  '''Returns a Dataframe of buys.csv'''
  buys_csv_path = os.path.dirname(__file__) + 'buys.csv'
  buys_dataframe = pd.read_csv(buys_csv_path)
  return buys_dataframe


if __name__ == "__main__":
  parser = get_parser()

  args = parser.parse_args()

  args_vals = get_arg_values(args)
  if not any(args_vals):
    parser.print_help()

  if args.current:
    get_portfolio_value(get_buys_dataframe())

  if args.report:
    print("report")



