import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(transactions, customers):
	t_clean = transactions.drop(columns=['cust_id'])
    cross_df = pd.merge(t_clean, customers, how='cross')
    columns = [
        'trans_id',
        'trans_amt',
        'date',
        'cust_id',
        'first_name',
        'last_name',
        'age'
    ]
    return cross_df[columns]