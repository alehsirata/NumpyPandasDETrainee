import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(input_df):
    result = input_df[(input_df['view_count'] > 1000000) & (input_df['release_year'] > 2018)]
    return result