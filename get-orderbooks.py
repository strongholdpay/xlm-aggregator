
# In terminal need to:
# pip install requests
# make a bot.py and put this code in
# https://github.com/ccxt/ccxt/tree/master/python standardized exchange data parsing
import os
import ccxt


def print_results(exchange_name, results):


	print('-----bids-----')
	for result in results['bids']:
		print([result[0], result[1], 'bid', exchange_name])

	print('-----asks-----')
	for result in results['asks']:
		print([result[0], result[1], 'ask', exchange_name])



def main():
	exchanges = [
		'binance',
		'bittrex',
		'bitcoincoid',
		'cex',
		'hitbtc',
		'kraken',
		'poloniex',

	]
	for exchange_name in exchanges:
		try:
			constructor = getattr(ccxt, exchange_name)
		except AttributeError:
			print('Exchange {} not found on ccxt'.format(exchange_name))
			continue
		exchange = constructor()
		results = exchange.fetch_order_book('XLM/BTC')
		print_results(exchange_name, results)
		#break

	#print(exchange.fetchMarkets())


if __name__ == "__main__":
	main()


# Ask Price, Bid Price, Order Size, Ticker Symbol XLM, Ticket Symbol BTC, Exchange Name, Timestamp
# Bid = Buy
# Ask = Sell
# Next step, export to DB and order by price
# For this sort of app, I'd probably use flask (web application framework for python) to fetch data and serve an api, then have some kind of javascript graph that gets data from the flask app to display
# you need to pick a database (postgres?), pick some kind of graphing library (probably in javascript) if you want graphs