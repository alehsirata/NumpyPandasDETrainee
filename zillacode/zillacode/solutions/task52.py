import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(df_star, df_planet):
	star_clean = df_star.rename(columns={
        'name': 'star_name',
        'color': 'star_color',
        'type': 'star_type',
        'distance': 'distance_star_earth'
    })
    planet_clean = df_planet.rename(columns={
        'name': 'planet_name',
        'type': 'planet_type',
        'distance': 'distance_planet_star'
    })
    merged_df = pd.merge(planet_clean, star_clean, left_on='star_id', right_on='id', how='inner')
    columns = [
        'distance_planet_star',
        'distance_star_earth',
        'planet_name',
        'planet_type',
        'star_color',
        'star_name',
        'star_type'
    ]
    return merged_df[columns]