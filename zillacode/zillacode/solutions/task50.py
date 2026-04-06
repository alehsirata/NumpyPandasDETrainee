import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(artifacts):
	filtered_df = artifacts[artifacts['Quantity'] > 100].copy()
    filtered_df['Material'] = filtered_df['Material'].str.upper()
    columns = [
        'ID',
        'Item',
        'Material',
        'Period',
        'Quantity'
    ]
    return filtered_df[columns]