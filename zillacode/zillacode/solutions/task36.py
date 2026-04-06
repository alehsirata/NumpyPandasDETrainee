import pandas as pd
import numpy as np
import datetime
import json
import math
import re


def etl(venture_capitalist_df, funded_startups_df):
    avg_df = funded_startups_df.groupby('vc_id').agg(
        avg_funding=('funding', 'mean')
    ).reset_index()


merged_df = pd.merge(avg_df, venture_capitalist_df, on='vc_id', how='inner')
filtered_df = merged_df[merged_df['avg_funding'] > merged_df['funding_limit']]

columns = [
    'avg_funding',
    'funding_limit',
    'vc_id',
    'vc_name'
]
return filtered_df[columns].reset_index(drop=True)