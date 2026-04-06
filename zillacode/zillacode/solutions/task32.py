import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(rides, visitors):
	avg_ratings = visitors.groupby('ride_id').agg(
        average_rating=('rating', 'mean')
    ).reset_index()
    merged_df = pd.merge(avg_ratings, rides, on='ride_id', how='inner')
    global_mean = merged_df['average_rating'].mean()
    global_std = merged_df['average_rating'].std()
    threshold = 2 * global_std
    merged_df['is_anomalous'] = (abs(merged_df['average_rating'] - global_mean) > threshold).astype(int)
    columns = [
        'average_rating',
        'capacity',
        'is_anomalous',
        'ride_id',
        'ride_name',
        'type'
    ]
    return merged_df[columns]