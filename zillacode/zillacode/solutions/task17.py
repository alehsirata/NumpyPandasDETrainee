import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(input_df):
    numbs = input_df['description'].str.extract(r'(\d+)', expand=False)
    input_df['age'] = numbs.fillna("")
    return input_df