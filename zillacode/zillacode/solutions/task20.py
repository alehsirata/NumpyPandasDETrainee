import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(projects, employees, equipment):
	start_dt = pd.to_datetime(projects['start_date'])
    end_dt = pd.to_datetime(projects['end_date'])
    projects['duration_days'] = (end_dt - start_dt).dt.days

    employees_agg = employees.groupby('project_id').agg(
        total_employees=('employee_id', 'count'),
        unique_roles=('role', 'nunique')
    ).reset_index()

    equipment_agg = equipment.groupby('project_id').agg(
        total_equipment_cost=('cost', 'sum')
    ).reset_index()

    merged_df = pd.merge(projects, employees_agg, on='project_id', how='left')
    merged_df = pd.merge(merged_df, equipment_agg, on='project_id', how='left')
    columns = [
        'project_id',
        'project_name',
        'start_date',
        'end_date',
        'duration_days',
        'total_employees',
        'unique_roles',
        'total_equipment_cost'
    ]
    return merged_df[columns]