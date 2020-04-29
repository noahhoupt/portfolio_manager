import argparse
from actions.current import print_portfolio_value

if __name__ == "__main__":
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

  args = parser.parse_args()

  args_vals = []
  for key in args.__dict__:
    args_vals.append(args.__dict__[key])

  if not any(args_vals):
    parser.print_help()

  if args.current:
    print_portfolio_value()

  if args.report:
    print("report")



