import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(transactions):
	df = transactions.sort_values(by=['customer_id', 'date']).copy()
    df['previous_product'] = df.groupby('customer_id')['product_id'].shift(1)
    df['date_and_product'] = df['date'].astype(str) + ' ' + df['previous_product'].fillna('None')
    df['previous_product'] = df['previous_product'].replace({np.nan: None})
    columns = [
        'customer_id',
        'product_id',
        'quantity',
        'date',
        'previous_product',
        'date_and_product'
    ]
    return df[columns]