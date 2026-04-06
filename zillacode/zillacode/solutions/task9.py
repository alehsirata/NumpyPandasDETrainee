import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(research_papers, authors):
    merged_df = pd.merge(authors, research_papers, on='paper_id', how='inner')
    merged_df = merged_df.sort_values(by=['paper_id', 'author_id'])
    merged_df['row_number'] = merged_df.groupby('paper_id').cumcount() + 1
    return merged_df[['paper_id', 'author_id', 'name', 'row_number']]