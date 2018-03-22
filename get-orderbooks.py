
# In terminal need to:
# pip install requests
# make a bot.py and put this code in
# https://github.com/ccxt/ccxt/tree/master/python standardized exchange data parsing
import os
import ccxt


def print_results(exchange_name, results):
	query_date = results['datetime']

	print('-----bids-----')
	for result in results['bids']:
		print([result[0], result[1], 'bid', exchange_name, query_date])

	print('-----asks-----')
	for result in results['asks']:
		print([result[0], result[1], 'ask', exchange_name, query_date])



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
		constructor = getattr(ccxt, exchange_name)
		exchange = constructor()
		results = exchange.fetch_order_book('XLM/BTC')
		#print(results.keys())
		# dict_keys(['bids', 'asks', 'timestamp', 'datetime'])
		#print(results['datetime'])
		#print(data)
		print_results(exchange_name, results)
		#break

	#print(exchange.fetchMarkets())


if __name__ == "__main__":
	main()


# Ask Price, Bid Price, Order Size, Ticker Symbol XLM, Ticket Symbol BTC, Exchange Name, Timestamp
# Bid = Buy
# Ask = Sell
