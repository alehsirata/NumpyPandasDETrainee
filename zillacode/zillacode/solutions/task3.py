import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(properties_df, landlords_df):
	properties_df = properties_df.drop_duplicates()
    landlords_df = landlords_df.drop_duplicates()
    rent = properties_df.groupby('landlord_id')['rent'].sum().reset_index()
    rent.columns = ['landlord_id', 'total_rental_income']
    merged_df = pd.merge(rent, landlords_df, on='landlord_id', how='inner')
    merged_df['landlord_name'] = merged_df['first_name'] + ' ' + merged_df['last_name']
	result = merged_df[['landlord_id', 'landlord_name', 'total_rental_income']]
    return result