import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(employees, payroll):
	merged_df = pd.merge(employees, payroll, on='employee_id', how='inner')
    merged_df['pay'] = np.where(
        merged_df['hours_worked'] > 40,
        (40 * merged_df['hourly_rate']) + ((merged_df['hours_worked'] - 40) * merged_df['hourly_rate'] * 1.5),
        merged_df['hours_worked'] * merged_df['hourly_rate']
    )
    return merged_df[['employee_id', 'name', 'pay', 'position']]