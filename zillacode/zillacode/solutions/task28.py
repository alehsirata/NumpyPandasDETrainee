import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(df1, df2):
	merged_df = pd.merge(df1, df2, on='product_id', how='inner')
    merged_df = merged_df.sort_values(by='manufacturing_date', ascending=True)
    merged_df['row_number'] = range(1, len(merged_df) + 1)
    columns = [
        'product_id',
        'manufacturing_date',
        'manufacturing_location',
        'product_name',
        'product_type',
        'row_number'
    ]
    return merged_df[columns]