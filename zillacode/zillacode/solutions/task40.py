import pandas as pd
import numpy as np
import datetime
import json
import math
import re


def etl(background_checks):
    df = background_checks.copy()

    def count_items(val):
        if pd.isna(val) or str(val).strip() == '':
            return 0
        return len(str(val).split(','))

    df['crime_count'] = df['criminal_record'].apply(count_items)
    df['jobs_count'] = df['employment_history'].apply(count_items)
    df['degrees_count'] = df['education_history'].apply(count_items)
    df['places_lived_count'] = df['address'].apply(count_items)
    columns = [
        'check_id',
        'crime_count',
        'degrees_count',
        'dob',
        'full_name',
        'jobs_count',
        'places_lived_count'
    ]
    return df[columns]