import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(MortgageDetails, UserMortgages):
	merged_df = pd.merge(UserMortgages, MortgageDetails, on='MortgageID', how='inner')
    agg_df = merged_df.groupby('MortgageType').agg(
        sum_interest=('InterestRate', 'sum'),
        count_users=('UserID', 'count')
    ).reset_index()
    agg_df['RateOfMortgage'] = agg_df['sum_interest'] / agg_df['count_users']
    return agg_df[['MortgageType', 'RateOfMortgage']]