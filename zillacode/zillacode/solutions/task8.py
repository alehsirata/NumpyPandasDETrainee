import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(calls_df, customers_df):
	result = calls_df.groupby('date').agg(
        num_customers=('cust_id', 'nunique'),
        total_duration=('duration', 'sum')
    ).reset_index()
    return result