import pandas as pd
import numpy as np
import datetime
import json
import math
import re


def etl(AnimalData, RegionData):
    merged_df = pd.merge(AnimalData, RegionData, on='Region', how='inner')
agg_df = merged_df.groupby(['Species', 'Climate']).agg(
    AvgAge=('Age', 'mean'),
    AvgWeight=('Weight', 'mean'),
    TotalAnimals=('ID', 'count')
).reset_index()

agg_df['AvgWeight'] = agg_df['AvgWeight'].astype(int)
columns = [
    'AvgAge',
    'AvgWeight',
    'Climate',
    'Species',
    'TotalAnimals'
]
return agg_df[columns]