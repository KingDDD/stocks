#!/usr/bin/env python3

import yfinance
import matplotlib.pyplot as plt
from datetime import datetime

spxl = yfinance.Ticker("SPXL")
drn = yfinance.Ticker("DRN")
#print(type(spxl.info))
#for section,metric in stock_info.items():
#  print(section, ":", metric)


stock_name = spxl.info['longName']
previous_close = spxl.info['previousClose']
current_price = spxl.info['navPrice']
#print(stock_name)
#print(previous_close)
#print(current_price)

#SPXL

my_spxl = {'buyPrice' : '95.92', 'buyDate' : '04/14/2021', 'principal' : '11030.84'}
numshares = int(float(my_spxl['principal'])/float(my_spxl['buyPrice']))
current_position_value = numshares * float(current_price)
diff = (current_position_value - float(my_spxl['principal']))

print(spxl.info['longName'])
print('Shares Held: ', numshares)
print('Total $ Gain: {:.2f}'.format(diff))

total_percent_gain = (diff/current_position_value) * 100

print('Total % Gain: {:.2f}'.format(total_percent_gain))
print()
#DRN
print(drn.info['longName'])
my_drn = {'buyPrice' : '18.45', 'buyDate' : '05/17/2021', 'principal' : '10152.10'}
numshares = int(float(my_drn['principal'])/float(my_drn['buyPrice']))
print('Shares Held: ', numshares)
current_postion_value = numshares * float(drn.info['navPrice'])
diff = (current_postion_value - float(my_drn['principal']))
print('Total $ Gain: {:.2f}'.format(diff))

total_percent_gain = (diff/current_postion_value) * 100

print('Total % Gain: {:.2f}'.format(total_percent_gain))
