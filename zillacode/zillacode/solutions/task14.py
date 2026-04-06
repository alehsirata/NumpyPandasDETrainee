import pandas as pd
import numpy as np
import datetime
import json
import math
import re


def etl(pe_firms, pe_funds, pe_investments):
    merged_df = pd.merge(pe_firms, pe_funds, on='firm_id', how='outer')
    merged_df = pd.merge(merged_df, pe_investments, on='fund_id', how='outer')
    merged_df = merged_df.dropna(how='all')

    columns = [
        'investment_id',
        'fund_id',
        'firm_id',
        'firm_name',
        'founded_year',
        'location',
        'fund_name',
        'fund_size',
        'fund_start_year',
        'fund_end_year',
        'company_name',
        'investment_amount',
        'investment_date'
    ]
    return merged_df[columns]