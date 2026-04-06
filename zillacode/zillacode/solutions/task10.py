import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(products, sales, inventory):
	sales_agg = sales.groupby('product_id').agg(
        total_quantity=('quantity', 'sum'),
        total_revenue=('revenue', 'sum')
    ).reset_index()
    inventory_agg = inventory.groupby('product_id').agg(
        total_stock=('stock', 'sum')
    ).reset_index()
    merged_df = pd.merge(products, sales_agg, on='product_id', how='left')
    merged_df = pd.merge(merged_df, inventory_agg, on='product_id', how='left')

    fill = ['total_quantity', 'total_revenue', 'total_stock']
    merged_df[fill] = merged_df[fill].fillna(0)
    merged_df['total_quantity'] = merged_df['total_quantity'].astype(int)
    merged_df['total_revenue'] = merged_df['total_revenue'].astype(int)
    merged_df['total_stock'] = merged_df['total_stock'].astype(int)
    result = [
        'product_id',
        'name',
        'category',
        'total_quantity',
        'total_revenue',
        'total_stock'
    ]
    return merged_df[result]