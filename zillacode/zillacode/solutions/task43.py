import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(observations, species):
	merged_df = pd.merge(observations, species, on='species_id', how='inner')
    top3_df = merged_df.nlargest(3, 'count', keep='all')
    columns = [
        'count',
        'location_id',
        'obs_id',
        'species_id',
        'species_name'
    ]
    return top3_df[columns]