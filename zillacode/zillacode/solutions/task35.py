import pandas as pd
import numpy as np
import datetime
import json
import math
import re


def etl(df_sales, df_products):
    merged_df = pd.merge(df_sales, df_products, on='product_id', how='inner')


agg_df = merged_df.groupby(['date', 'product_category']).agg(
    total_quantity=('quantity_sold', 'sum')
).reset_index()
agg_df = agg_df.sort_values(by=['date', 'product_category']).reset_index(drop=True)
agg_df['date'] = agg_df['date'].astype(str)

columns = [
    'date',
    'product_category',
    'total_quantity'
]
return agg_df[columns]