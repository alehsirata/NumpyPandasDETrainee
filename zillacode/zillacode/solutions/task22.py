import pandas as pd
import numpy as np
import datetime
import json
import math
import re


def etl(user_behavior_df, subscription_df):
    user = user_behavior_df.copy()


sub = subscription_df.copy()
user['event_id'] = user.index
sub['subscriptionEnd'] = sub['subscriptionEnd'].replace('ongoing', '2100-01-01')
user['date'] = pd.to_datetime(user['date'])
sub['subscriptionStart'] = pd.to_datetime(sub['subscriptionStart'])
sub['subscriptionEnd'] = pd.to_datetime(sub['subscriptionEnd'])
merged_df = pd.merge(user, sub, on='userId', how='inner')

active_watches = merged_df[
    (merged_df['date'] >= merged_df['subscriptionStart']) &
    (merged_df['date'] <= merged_df['subscriptionEnd'])
    ]
active_watches = active_watches.drop_duplicates(subset=['event_id'])

result_df = active_watches.groupby('userId').agg(
    totalWatchTime=('watchDuration', 'sum')
).reset_index()
return result_df[['userId', 'totalWatchTime']]