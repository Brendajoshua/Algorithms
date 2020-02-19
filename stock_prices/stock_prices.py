#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_profit = float('-inf')
  min_price = float('inf')

  for i in range(len(prices) - 1):
    #check against current min price
    if prices[i] < min_price:
      min_price = prices[i]
      #compare current price against all remaining prices
      for j in range(i + 1, len(prices) - 1):
        current_profit = prices[j] - prices[i]
        #compare against current max profit
        if current_profit > max_profit:
          max_profit = current_profit

  return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))