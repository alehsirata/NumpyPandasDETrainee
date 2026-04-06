import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(movies_df):
	result = movies_df[movies_df['box_office_collection'].isna()]
    return result