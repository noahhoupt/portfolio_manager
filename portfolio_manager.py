import argparse

if __name__ == "__main__":
  parser = argparse.ArgumentParser(
    description="It tracks statistics related to your stock portfolio in real time"
  )
  parser.add_argument(
    "-c",
    "--current",
    action='store_true',
    default=True,
    help="Prints current value of portfolio"
  )
  parser.add_argument(
    "-r",
    "--report",
    action='store_true',
    default=True,
    help="Stores value of current portfolio in report.txt file"
  )

  args = parser.parse_args()

  print(args._get_args())

  if not any(args._get_args()):
    parser.print_help()

  if args.current:
    print("current")

  if args.report:
    print("report")



