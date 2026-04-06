import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(df_math_expr):
    valid_df = df_math_expr[df_math_expr['expression'].str.match(r'^\d+([\+\-\*\/]\d+)+$')].copy()
    return valid_df[['expression', 'id']]