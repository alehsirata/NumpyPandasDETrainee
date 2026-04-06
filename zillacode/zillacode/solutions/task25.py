import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(mines, extraction):
	merged_df = pd.merge(mines, extraction, left_on='id', right_on='mine_id', how='inner')
    grouped_df = merged_df.groupby(['location', 'mineral']).agg(
        total_quantity=('quantity', 'sum')
    ).reset_index()
    columns = ['location', 'mineral', 'total_quantity']
    return grouped_df[columns]