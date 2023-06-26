"""
'Assignment'
Create a script which will generate a report on Profit and loss statement of share market portfolio.
Get input from the user in csv file. Csv file will have 3 columns Company Name, Rate per share, quantity of share.
The script should make a call to BSE API and get the current/LTP (last trading prize) of that company share.
Get the mapping of company name and the BSE stock code from
the URL https://static.quandl.com/BSE+Descriptions/stocks.txt
Generate a statement of Profit and Loss as well calculate the deviation from purchase price to current price.
Log the data into another text file. The log data should contain the company name and day high price of that stock.
You an use pandas for this assignment
"""

import pandas as pd
from bsedata.bse import BSE
import logging
from bsedata.exceptions import InvalidStockException


def get_stock_code(company_name, stock_data):
    for code, name in stock_data.items():
        if name == company_name:
            return code
    return None


def get_current_price(stock_code, bse):
    try:
        stock_info = bse.getQuote(stock_code)
        # print(stock_info)
        current_price = stock_info['currentValue'] if stock_info else None
        high_price = stock_info['dayHigh'] if stock_info else None
        low_price = stock_info['dayLow'] if stock_info else None
        return current_price, high_price, low_price
    except InvalidStockException:
        return None, None, None


def generate_profit_loss(csv_files):
    df = pd.read_csv(csv_file)
    bse = BSE()
    stock_data = bse.getScripCodes()
    # print(stock_data)
    logging.basicConfig(filename='profit_loss.log', level=logging.INFO, format='%(message)s')
    total_purchase_amount = 0
    total_current_amount = 0
    for index, row in df.iterrows():
        company_name = row['Company Name']
        rate_per_share = row['Rate per Share']
        quantity = row['Quantity']
        stock_code = get_stock_code(company_name, stock_data)
        if stock_code is None:
            logging.error(f'Stock code not found for company: {company_name}. Please check you csv file')
            continue
        current_price, high_price, low_price = get_current_price(stock_code, bse)
        if current_price is None:
            logging.error(f'Unable to fetch current price for company: {company_name}.')
            continue
        rate_per_share = float(rate_per_share)
        quantity = int(quantity)
        purchase_amount = rate_per_share * quantity
        current_amount = float(current_price) * quantity
        deviation = current_amount - purchase_amount
        total_purchase_amount += purchase_amount
        total_current_amount += current_amount
        profit_loss_percentage = (deviation / purchase_amount) * 100
        logging.info(f'Company: {company_name}, Deviation of Stocks: {deviation:.2f}, '
                     f'Profit/Loss Percentage of Stocks: {profit_loss_percentage:.2f}%, '
                     f'Current Stock Price(LTP): {current_price}, '
                     f'High Price of Stocks in a Day: {high_price}, Low Price of Stocks in a Day: {low_price}')
    overall_deviation = total_current_amount - total_purchase_amount
    overall_profit_loss_percentage = (overall_deviation / total_purchase_amount) * 100
    logging.info(f'Overall Deviation of Stocks: {overall_deviation:.2f}, '
                 f'Overall Profit/Loss Percentage of Stocks: {overall_profit_loss_percentage:.2f}%')
    print('Report file generated successfully. Please check "profit_loss.log" for details.')


csv_file = 'portfolio.csv'
generate_profit_loss(csv_file)
