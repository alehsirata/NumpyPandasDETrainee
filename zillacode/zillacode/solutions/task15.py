import pandas as pd
import numpy as np
import datetime
import json
import math
import re


def etl(pages):
    sorted_df = pages.sort_values(by='seo_score', ascending=False)


domain_best = sorted_df.drop_duplicates(subset=['domain'], keep='first').copy()
domain_best = domain_best.rename(columns={
    'url': 'highest_seo_page',
    'seo_score': 'highest_seo_score'
})
overall_max_score = domain_best['highest_seo_score'].max()

domain_best['overall_highest_page'] = np.where(
    domain_best['highest_seo_score'] == overall_max_score,
    domain_best['highest_seo_page'],
    None
)

domain_best['overall_highest_score'] = np.where(
    domain_best['highest_seo_score'] == overall_max_score,
    domain_best['highest_seo_score'],
    np.nan
)
final_columns = [
    'domain',
    'highest_seo_page',
    'highest_seo_score',
    'overall_highest_page',
    'overall_highest_score'
]

return domain_best[final_columns].sort_values(by='domain').reset_index(drop=True)