import pandas as pd
import numpy as np
import datetime
import json
import math
import re


def etl(df_models, df_usage):
    df_models['Average_Accuracy'] = df_models.groupby('Model_Type')['Accuracy'].transform('mean')
    df_usage_agg = df_usage.groupby('Model_ID').agg(
        Total_Uses=('Uses', 'sum')
    ).reset_index()


merged_df = pd.merge(df_models, df_usage_agg, on='Model_ID', how='inner')
columns = [
    'Model_ID',
    'Model_Name',
    'Model_Type',
    'Accuracy',
    'Total_Uses',
    'Average_Accuracy'
]

return merged_df[columns]