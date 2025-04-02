import sys
import os
sys.path.append(os.path.abspath("c:/Users/nikap/Documents/Snpectinatus/"))
import numpy as np
import pandas as pd
from create_and_clean_dataset import load_data as ld, clear_duplicates as cd, adjust_prices as ap, remove_prices_below_1e_8 as rpb

# 1. Load data from the CSV file
prices = ld.load_data() 
# 2. Remove duplicates
prices = cd.clear_duplicates(prices)
# 3. Adjust prices
ap.adjust_prices(prices)
# 4. Filter out rows where any price column is below 1e-8
prices=rpb.remove_prices_below_1e8(prices)
# 5. Remove penny stocks