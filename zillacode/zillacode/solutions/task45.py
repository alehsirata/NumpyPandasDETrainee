import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(df1, df2):
	df = pd.concat([df1, df2], ignore_index=True)
    df = df.sort_values(by=['Country', 'Year']).reset_index(drop=True)
    df['GDP_growth_rate'] = (df.groupby('Country')['GDP'].pct_change() * 100).round(2)
    return df[['Country', 'GDP_growth_rate', 'Year']]