import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(df_experiments, df_materials):
	merged_df = pd.merge(df_experiments, df_materials, on='material_id', how='outer')
    merged_df = merged_df.sort_values(by='experiment_id').reset_index(drop=True)
    columns = [
        'experiment_date',
        'experiment_id',
        'experiment_results',
        'material_id',
        'material_name',
        'material_type'
    ]
    return merged_df[columns]