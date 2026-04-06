import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(products_df, orders_df):
	merged_df = pd.merge(products_df, orders_df, on='product_id', how='inner')
    result = merged_df.groupby('category').agg(
        avg_price = ('price', 'mean'),
        total_orders_count = ('quantity', 'count')
    ).reset_index()
    return result[['avg_price', 'category', 'total_orders_count']]