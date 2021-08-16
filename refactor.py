#!/usr/bin/env python3

import yfinance

spxl = yfinance.Ticker("SPXL")
drn = yfinance.Ticker("DRN")
coke = yfinance.Ticker("COKE")
bxmt = yfinance.Ticker("BXMT")

MY_SPXL = {'buyPrice': '95.92', 'buyDate': '04/14/2021',
           'principal': '11030.84'}
MY_DRN = {'buyPrice': '18.45', 'buyDate': '05/17/2021',
          'principal': '10152.10'}
MY_COKE = {'buyPrice': '378.90', 'buyDate': '05/25/2021',
           'principal': '4925.79'}
MY_BXMT = {'buyPrice': '31.93', 'buyDate': '07/02/2021',
           'principal': '4789.50'}


def figure(ticker, position):
    stock = ticker
    my_pos = position

    current_stock = {}

    stock_name = stock.info['longName']
    previous_close = stock.info['previousClose']
    current_price = stock.info['navPrice']

    # # of shares in position
    numshares = int(float(my_pos['principal'])/float(my_pos['buyPrice']))
    # total Value of position
    if current_price is not None:
        current_position_value = numshares * float(current_price)
    else:
        current_price = previous_close
        current_position_value = numshares * float(current_price)
    # total monetary gain
    gain = (current_position_value - float(my_pos['principal']))
    # total percentage gain
    total_percent_gain = (gain/current_position_value) * 100

    # daily percentage gain
    # daily dollar gain
    if current_price >= previous_close:
        daily_p_gain = (1 - previous_close/current_price) * 100
        daily_dollar = (current_price - previous_close) * numshares
    else:
        daily_dollar = (previous_close - current_price) * numshares
        daily_p_gain = (1 - current_price/previous_close) * 100

    # build dictionary
    current_stock["Ticker: "] = stock_name
    current_stock["Number of Shares: "] = int(numshares)
    current_stock["Total Position Value: $$"] = current_position_value
    current_stock["Daily Gain: $$"] = daily_dollar
    current_stock["Daily Percentage Change: %%"] = daily_p_gain
    current_stock["Total Gain: $$"] = gain
    current_stock["Total Percentage Gain: %%"] = total_percent_gain

    return current_stock


def format_output(obj):
    output = obj
    for key, value in output.items():
        if isinstance(value, float):
            print(key, "{:.2f}".format(value))
        else:
            print(key, value)

    print()


def main():

    working_dict = {}
    working_dict = figure(spxl, MY_SPXL)
    format_output(working_dict)

    working_dict = figure(drn, MY_DRN)
    format_output(working_dict)

    working_dict = figure(coke, MY_COKE)
    format_output(working_dict)

    working_dict = figure(bxmt, MY_BXMT)
    format_output(working_dict)


main()
