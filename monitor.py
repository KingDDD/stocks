#!/usr/bin/env python3

import yfinance
import matplotlib.pyplot as plt
from datetime import datetime

spxl = yfinance.Ticker("SPXL")
drn = yfinance.Ticker("DRN")
#print(type(spxl.info))

spxl_info = spxl.info
drn_info = drn.info
#for section,metric in stock_info.items():
#  print(section, ":", metric)


stock_name = spxl_info['longName']
previous_close = spxl_info['previousClose']
current_price = spxl_info['navPrice']
#print(stock_name)
#print(previous_close)
#print(current_price)

#SPXL
print(spxl_info['longName'])
my_spxl = {'buyPrice' : '95.92', 'buyDate' : '04/14/2021', 'principal' : '11030.84'}
numshares = int(float(my_spxl['principal'])/float(my_spxl['buyPrice']))
print('Shares Held: ', numshares)
current_position_value = numshares * float(current_price)
diff = (current_position_value - float(my_spxl['principal']))
print('Total $ Gain: {:.2f}'.format(diff))

total_percent_gain = (diff/current_position_value) * 100

print('Total % Gain: {:.2f}'.format(total_percent_gain))
print()
#DRN
print(drn_info['longName'])
my_drn = {'buyPrice' : '18.45', 'buyDate' : '05/17/2021', 'principal' : '10152.10'}
numshares = int(float(my_drn['principal'])/float(my_drn['buyPrice']))
print('Shares Held: ', numshares)
current_postion_value = numshares * float(drn_info['navPrice'])
diff = (current_postion_value - float(my_drn['principal']))
print('Total $ Gain: {:.2f}'.format(diff))

total_percent_gain = (diff/current_postion_value) * 100

print('Total % Gain: {:.2f}'.format(total_percent_gain))
