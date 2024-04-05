import yahoo_fin.stock_info as si
import pandas as pd

val = si.get_stats_valuation('aapl')
 
val = val.iloc[:,:2]
 
val.columns = ["Attribute", "Recent"]

