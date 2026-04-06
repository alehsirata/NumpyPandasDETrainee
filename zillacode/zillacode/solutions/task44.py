import pandas as pd
import numpy as np
import datetime
import json
import math
import re


def etl(portfolio, prices):
    merged_df = pd.merge(portfolio, prices, on='company', how='inner')
merged_df['position_value'] = merged_df['shares'] * merged_df['closing_price']

portfolio_df = merged_df.groupby(['PE_firm', 'date']).agg(
    portfolio_value=('position_value', 'sum')
).reset_index()
portfolio_df['portfolio_value'] = portfolio_df['portfolio_value'].astype(int)
portfolio_df['date'] = portfolio_df['date'].astype(str)
portfolio_df = portfolio_df.sort_values(by=['PE_firm', 'date'])
columns = [
    'PE_firm',
    'date',
    'portfolio_value'
]

return portfolio_df[columns]