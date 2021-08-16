#!/usr/bin/env python3

import yfinance
from datetime import date
import matplotlib.pyplot as plt

spxl = yfinance.Ticker("SPXL")
MY_SPXL = {'buyPrice': '95.92',
           'buyDate': '2021-04-14',
           'principal': '11030.84'}

drn = yfinance.Ticker("DRN")
MY_DRN = {'buyPrice': '18.45',
          'buyDate': '2021-05-17',
          'principal': '10152.10'}

coke = yfinance.Ticker("COKE")
MY_COKE = {'buyPrice': '378.90',
           'buyDate': '2021-05-25',
           'principal': '4925.79'}

bxmt = yfinance.Ticker("BXMT")
MY_BXMT = {'buyPrice': '31.93',
           'buyDate': '2021-07-02',
           'principal': '4789.50'}


class Big_Brain():

    def figure(self, ticker, position):

        self.stock = ticker
        self.my_pos = position
        current_stock = {}

        stock_name = self.stock.info['longName']
        previous_close = self.stock.info['previousClose']
        current_price = self.stock.info['navPrice']

        # # of shares in position
        numshares = int(float(self.my_pos['principal']) /
                        float(self.my_pos['buyPrice']))
        # total Value of position
        if current_price is not None:
            current_position_value = numshares * float(current_price)
        else:
            current_price = previous_close
            current_position_value = numshares * float(current_price)
        # total monetary gain
        gain = (current_position_value - float(self.my_pos['principal']))
        # total percentage gain
        total_percent_gain = (gain/current_position_value) * 100

        # daily percentage gain & daily dollar gain
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

    def format_output(self, obj):

        output = obj
        for key, value in output.items():
            if isinstance(value, float):
                print(key, "{:.2f}".format(value))
            else:
                print(key, value)

        # plotter(figure.stock, figure.my_pos)
        print()

    def plotter(self, ticker, my_pos):

        stock = self.stock
        my_position = self.my_pos
        today = date.today()
        data = yfinance.download(stock.info['symbol'],
                                 my_position['buyDate'],
                                 today)
        data['Adj Close'].plot()
        plt.title(stock.info['symbol'])
        plt.show()


def main():

    working_dict = {}
    brain = Big_Brain()

    working_dict = brain.figure(spxl, MY_SPXL)
    brain.format_output(working_dict)
    brain.plotter(spxl, MY_SPXL)

    working_dict = brain.figure(drn, MY_DRN)
    brain.format_output(working_dict)
    brain.plotter(drn, MY_DRN)

    working_dict = brain.figure(coke, MY_COKE)
    brain.format_output(working_dict)
    brain.plotter(coke, MY_COKE)

    working_dict = brain.figure(bxmt, MY_BXMT)
    brain.format_output(working_dict)
    brain.plotter(bxmt, MY_BXMT)


main()
