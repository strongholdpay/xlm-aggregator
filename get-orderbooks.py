
# In terminal need to:
# pip install requests

# make a bot.py and put this code in
# https://github.com/ccxt/ccxt/tree/master/python standardized exchange data parsing
import os
import requests
import ccxt


def get_order_book(url):
	response = requests.get(url)
	data = {}
	if response.status_code != 200:
		print('Error! {}'.format(response.status_code))
	else:
		data = response.json()
	return data


def parse_binance_data(exchange_name, raw_data):
	print(raw_data)
	print(raw_data.keys())
	# dict_keys(['lastUpdateId', 'bids', 'asks' 'price', 'qty'])
	bids = raw_data['bids']
	print(bids)
	ask_price = raw_data['']
	bid_price = raw_data['']
	order_size = raw_data['']
	volume = raw_data['']
	ticker_symbol_xlm = raw_data['']
	ticker_symbol_btc = raw_data['']
	timestamp = raw_data['']
	return [exchange_name, ask_price, bid_price, order_size, ticker_symbol_xlm, ticker_symbol_btc, timestamp]

def parse_bittrex_data(exchange_name, raw_data):
	bid_data = raw_data['result']['buy']
	print(bid_data)
	# {'Quantity': 834.72615344, 'Rate': 2.652e-05}
	#print(bid_data.keys())
	# dict_keys(['lastUpdateId', 'bids', 'asks'])
	result_data = []
	for bid in bid_data:
		row_data = [exchange_name, None, bid['Rate'], bid['Quantity'], None, None, None, None]
		result_data.append(row_data)
	return result_data
	# All price data is in BTC


def main():
	exchanges = [
		#('https://www.binance.com/api/v1/depth?symbol=XLMBTC', 'binance', parse_binance_data),
		('https://bittrex.com/api/v1.1/public/getorderbook?market=BTC-XLM&type=both', 'bittrex', parse_bittrex_data),
		#('https://api.hitbtc.com/api/2/public/orderbook/xlmbtc', 'hitbtc', parse_hitbtc_data),
		#('https://api.kraken.com/0/public/Depth?pair=XLMXBT', 'kraken', parse_kraken_data),
		#('https://poloniex.com/public?command=returnOrderBook&currencyPair=BTC_STR', 'poloniex', parse_poloniex_data),

	]
	for exchange in exchanges:
		url = exchange[0]
		exchange_name = exchange[1]
		parsing_function = exchange[2]
		raw_data = get_order_book(url)
		parsed_data = parsing_function(exchange_name, raw_data)
		print(parsed_data)
		#print(data)

	print(ccxt.exchanges)


if __name__ == "__main__":
	main()


# Ask Price, Bid Price, Order Size, Volume, Ticker Symbol XLM, Ticket Symbol BTC, Exchange Name, Timestamp

# Bid = Buy
# Ask = Sell
