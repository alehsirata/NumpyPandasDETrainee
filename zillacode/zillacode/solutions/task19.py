import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(companies, investments):
	merged_df = pd.merge(companies, investments, on='company_id', how='inner')
    result = merged_df.groupby('industry').agg(
        total_investment = ('amount', 'sum')
    ).reset_index()
    return result[['industry', 'total_investment']]