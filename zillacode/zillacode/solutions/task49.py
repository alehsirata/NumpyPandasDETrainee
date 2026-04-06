import pandas as pd
import numpy as np
import datetime
import json
import math
import re


def etl(flights, airports, planes):
    df = pd.merge(flights, planes, left_on='flight_id', right_on='plane_id', how='inner')
df = pd.merge(df, airports, left_on='origin_airport', right_on='airport_id', how='inner')
df = df.rename(columns={'airport_name': 'origin_name'})
df = df.drop(columns=['airport_id'])
df = pd.merge(df, airports, left_on='destination_airport', right_on='airport_id', how='inner')
df = df.rename(columns={'airport_name': 'dest_name'})

df['origin_airport_name_length'] = df['origin_name'].str.strip().str.len().astype(int)
df['destination_airport_name_length'] = df['dest_name'].str.strip().str.len().astype(int)
df['plane_model_length'] = df['plane_model'].str.strip().str.len().astype(int)

columns = [
    'destination_airport_name_length',
    'flight_id',
    'origin_airport_name_length',
    'plane_model_length'
]
return df[columns]