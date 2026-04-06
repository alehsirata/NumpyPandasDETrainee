import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(customers, orders, products):
	merged_df = pd.merge(orders, customers, on='customer_id', how='left')
    merged_df = pd.merge(merged_df, products, on='product_id', how='left')
	merged_df['customer_name'] = merged_df['first_name'] + ' ' + merged_df['last_name']
    final_columns = [
        'category',
        'customer_name',
        'email',
        'order_date',
        'order_id',
        'product_name',
    ]
    return merged_df[final_columns]