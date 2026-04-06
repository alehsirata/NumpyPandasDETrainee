import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(input_df):
	self_interactions = input_df[input_df['user1_id'] == input_df['user2_id']]
    result = self_interactions.groupby('user1_id').size().reset_index(name='self_interaction_count')
    return result[['user1_id', 'self_interaction_count']]