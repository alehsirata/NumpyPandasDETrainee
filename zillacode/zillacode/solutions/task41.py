import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(buildings):
	df = buildings.copy()
    df['avg_height_per_floor'] = np.where(
        df['floors'] == 0,
        0.0,
        (df['height_m'] / df['floors']).round(2)
    )
    df = df.sort_values(by='avg_height_per_floor', ascending=True).reset_index(drop=True)
    columns = [
        'avg_height_per_floor',
        'city',
        'country',
        'id',
        'name'
    ]
    return df[columns]