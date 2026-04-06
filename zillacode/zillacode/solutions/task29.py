import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(budget_df, spending_df):
	b_agg = budget_df.groupby('Department').agg(
        Budget_Variance=('Budget', 'var')
    ).reset_index()
    s_agg = spending_df.groupby('Department').agg(
        Spending_Variance=('Spending', 'var')
    ).reset_index()
    merged_df = pd.merge(b_agg, s_agg, on='Department', how='inner')
    merged_df['Budget_Variance'] = merged_df['Budget_Variance'].fillna(0).astype(int)
    merged_df['Spending_Variance'] = merged_df['Spending_Variance'].fillna(0).astype(int)
    return merged_df[['Department', 'Budget_Variance', 'Spending_Variance']]