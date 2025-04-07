import sys
import os
sys.path.append(os.path.abspath("c:/Users/nikap/Documents/Snpectinatus/"))
import numpy as np
import pandas as pd
from create_and_clean_dataset import load_data as ld, \
clear_duplicates as cd, \
adjust_prices as ap, \
remove_prices_below_1e_8 as rpb, \
remove_penny_stocks as rps,\
calculate_return_per_symbol_ptc_change as crp, \
calculate_market_returns_SPY as cmr, \
clear_stocks_younger_than_a_year as csy, \
calculate_dollar_value_month as cdvm, \
calculate_liquidity as cl \

# 1. Load data from the CSV file
prices = ld.load_data() 
# 2. Remove duplicates
prices = cd.clear_duplicates(prices)
# 3. Adjust prices
ap.adjust_prices(prices)
# 4. Filter out rows where any price column is below 1e-8
#prices=rpb.remove_prices_below_1e8(prices)
# 5. Remove penny stocks (last stock price below 5$)
prices=rps.remove_penny_stocks(prices)
# 6. Calculate returns
crp.calculate_returns(prices)
#7. Remove stocks with less than 253 observations (1 year of data). 
# This is because the momentum will be calculated with T-12 comparison to T-1
prices=csy.clear_stocks_younger_than_a_year(prices)
#8. Calculate market returns for SPY
prices=cmr.calculate_market_returns_SPY(prices)
#9. Calculate dollar value per month
prices=cdvm.calculate_dollar_value_month(prices)
#10.Calculate liquidity
print(prices)
prices=cl.calculate_liquidity(prices, 1000)
print(prices)

prices[prices['liquid_1000'] == 1].to_csv(r'C:\Users\nikap\Documents\Snpectinatus\Seasonality results\prices_liquid.csv')
print(prices[prices['liquid_1000'] == 1])
print(prices[prices['liquid_1000']['symbol'].unique()])