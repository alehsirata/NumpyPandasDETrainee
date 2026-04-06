import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(df_temperature, df_pressure):
	merged_df = pd.merge(df_temperature, df_pressure, on='ExperimentID', how='inner')
    merged_df['Result'] = merged_df['Temperature'] * merged_df['Pressure']
    merged_df = merged_df.sort_values(by='ExperimentID', ascending=True).reset_index(drop=True)
    return merged_df[['ExperimentID', 'Result']]