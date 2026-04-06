import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(df_orders, df_products):
	merged_df = pd.merge(df_orders, df_products, on='product_id', how='inner')
    merged_df['temp_date'] = pd.to_datetime(merged_df['order_date'], format='%m/%d/%Y', errors='coerce')
    merged_df = merged_df.dropna(subset=['temp_date'])
    merged_df['is_weekend'] = merged_df['temp_date'].dt.dayofweek.isin([5, 6])
    columns = [
        'user_id',
        'product_name',
        'category',
        'order_date',
        'is_weekend'
    ]
    return merged_df[columns]