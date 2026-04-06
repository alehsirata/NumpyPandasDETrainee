import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(input_df1, input_df2):
	result = pd.concat([input_df1, input_df2], ignore_index=True)
    return result