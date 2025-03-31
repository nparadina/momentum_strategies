import sys
import os
sys.path.append(os.path.abspath("c:/Users/nikap/Documents/Snpectinatus/"))
from create_and_clean_dataset import load_data as ld, clear_duplicates as cd, adjust_prices as ap

# 1. Load data from the CSV file
prices = ld.load_data() 
# 2. Remove duplicates
prices=clear_duplicates = cd.clear_duplicates(prices)
# 3. Adjust prices
ap.adjust_prices(prices)
print(prices)