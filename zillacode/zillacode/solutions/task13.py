import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(mountain_info, mountain_climbers):
	merged_df = pd.merge(
        mountain_info,
        mountain_climbers,
        left_on='name',
        right_on='mountain_name',
        how='inner'
    )
    merged_df = merged_df.sort_values(by='climb_date', ascending=False)
    result = merged_df.drop_duplicates(subset=['mountain_name'], keep='first')
    return result[['climb_date', 'climb_time', 'climber_name', 'mountain_name']]