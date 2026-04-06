import pandas as pd
import numpy as np
import datetime
import json
import math
import re


def etl(df1, df2):
    df2['maintenance_cost_rank'] = df2.groupby('equipment_id')['maintenance_cost'].rank(method='dense',
                                                                                        ascending=False).astype(int)
df2_sorted = df2.sort_values(by=['equipment_id', 'maintenance_date'], ascending=[True, False])
df2_latest = df2_sorted.drop_duplicates(subset=['equipment_id'], keep='first').copy()
df2_latest = df2_latest.rename(columns={'maintenance_date': 'latest_maintenance_date'})
merged_df = pd.merge(df1, df2_latest, on='equipment_id', how='inner')
merged_df['latest_maintenance_date'] = merged_df['latest_maintenance_date'].astype(str)
merged_df['purchase_date'] = merged_df['purchase_date'].astype(str)

columns = [
    'equipment_id',
    'equipment_name',
    'latest_maintenance_date',
    'maintenance_cost_rank',
    'purchase_date'
]
return merged_df[columns]