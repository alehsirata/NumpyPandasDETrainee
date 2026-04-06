import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(products_df, manufacturing_processes_df):
	products_clean = products_df.drop_duplicates()
    processes_clean = manufacturing_processes_df.drop_duplicates()
    merged_df = pd.merge(products_clean, processes_clean, on='ProductID', how='inner')
    columns = [
        'ProductID',
        'ProductName',
        'Category',
        'ProcessID',
        'ProcessName',
        'Duration'
    ]
    return merged_df[columns]