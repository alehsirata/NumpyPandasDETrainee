import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(products, sales):
	merged_df = pd.merge(products, sales, on='product_id', how='inner')
    df = merged_df.groupby(['category', 'product_name'])['revenue'].sum().reset_index()
    df['rank'] = df.groupby('category')['revenue'].rank(method='dense', ascending=False).astype(int)
    top3_df = df[df['rank'] <= 3].copy()
    top3_df['revenue'] = top3_df['revenue'].astype(int)
    top3_df = top3_df.sort_values(by=['category'])
    final_columns = ['category', 'product_name', 'revenue', 'rank']
    return top3_df[final_columns]