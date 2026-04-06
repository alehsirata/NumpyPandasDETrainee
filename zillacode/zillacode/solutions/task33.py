import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(aerospace_df, company_df):
	a_df = aerospace_df.rename(columns={
        'name': 'equipment_name',
        'type': 'equipment_type',
        'status': 'equipment_status'
    })
    c_df = company_df.rename(columns={
        'id': 'company_id',
        'name': 'company_name'
    })
    merged_df = pd.merge(a_df, c_df, on='company_id', how='inner')
    conditions = [
        (merged_df['equipment_status'] == 'active') & (merged_df['country'] == 'USA'),
        (merged_df['equipment_status'] == 'active') & (merged_df['country'] != 'USA')
    ]
    choices = ['Domestic Active', 'Foreign Active']
    merged_df['status_label'] = np.select(conditions, choices, default='Inactive')
    columns = [
        'company_name',
        'country',
        'equipment_name',
        'equipment_status',
        'equipment_type',
        'id',
        'status_label'
    ]
    return merged_df[columns]