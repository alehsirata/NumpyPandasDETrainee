import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(input_df):
	input_df['email_domain'] = input_df['email'].str.split('@').str[1]
    phone_str = input_df['phone'].astype(str)
    input_df['anon_phone'] = '******' + phone_str.str[-4:]
    result_df = input_df[['anon_phone', 'email_domain', 'user_id']]
    return result_df