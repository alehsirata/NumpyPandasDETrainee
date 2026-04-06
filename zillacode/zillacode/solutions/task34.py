import pandas as pd
import numpy as np
import datetime
import json
import math
import re


def etl(page_visits, page_likes, page_comments):
    v = page_visits.rename(columns={'visit_time': 'interaction_time'}).copy()
v['interaction_type'] = 'visit'
l = page_likes.rename(columns={'like_time': 'interaction_time'}).copy()
l['interaction_type'] = 'like'
c = page_comments.rename(columns={'comment_time': 'interaction_time'}).copy()
c['interaction_type'] = 'comment'
combined_df = pd.concat([v, l, c], ignore_index=True)

combined_df['interaction_time'] = pd.to_datetime(combined_df['interaction_time'])
combined_df = combined_df.sort_values(by='interaction_time').reset_index(drop=True)
combined_df['interaction_time'] = combined_df['interaction_time'].astype(str)

columns = [
    'user_id',
    'page_id',
    'interaction_time',
    'interaction_type'
]
return combined_df[columns]