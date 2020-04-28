# portfolio_manager

It tracks statistics related to your stock portfolio in real time.

## buys.csv File Format

Create a file named `buys.csv` at the root directory of this repository. This file represents the stock buys in your portfolio. 

The format of the `.csv` file is as follows:
```
[stock1_ticker],[stock1_average_cost],[stock1_share_count]
[stock2_ticker],[stock2_average_cost],[stock2_share_count]
#stock3
#etc.
```

For example, if my portfolio consisted of 3 shares of Amazon (AMZN) at $2000, and 2 shares of Facebook (FB) at $150, my `buys.csv` file would look at follow:
```
AMZN,2000,3
FB,150,2
```

Decimals are valid input for columns 2 and 3.
