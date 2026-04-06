import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(social_media):
	social_media['text'] = social_media['text'].str.replace('Python', 'PySpark')
    return social_media