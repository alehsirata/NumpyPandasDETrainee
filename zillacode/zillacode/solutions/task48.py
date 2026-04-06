import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(customers, orders, products):
	customers[['first_name', 'last_name']] = customers['full_name'].str.split(' ', n=1, expand=True)
    products[['product_type', 'product_color']] = products['product_info'].str.split(',', n=1, expand=True)
    merged_df = pd.merge(orders, customers, on='customer_id', how='left')
    merged_df = pd.merge(merged_df, products, on='product_id', how='left')
    columns = [
        'customer_id',
        'first_name',
        'last_name',
        'location',
        'order_id',
        'product_color',
        'product_id',
        'product_type',
        'quantity'
    ]
    return merged_df[columns]