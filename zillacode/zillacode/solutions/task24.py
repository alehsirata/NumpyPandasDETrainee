import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(df_accounts, df_activities, df_exit_surveys):
	df_activities_clean = df_activities.drop_duplicates()
    merged_df = pd.merge(df_accounts, df_activities_clean, on='user_id', how='outer')
    merged_df = pd.merge(merged_df, df_exit_surveys, on='user_id', how='outer')
    merged_df = merged_df.sort_values(
        by=['user_id', 'activity_date'],
        ascending=[True, False]
    ).reset_index(drop=True)
    columns = [
        'user_id',
        'account_created_date',
        'location',
        'activity_date',
        'activity_type',
        'exit_date',
        'exit_reason'
    ]
    return merged_df[columns]