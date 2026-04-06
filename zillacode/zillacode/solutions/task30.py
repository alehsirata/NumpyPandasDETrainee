import pandas as pd
import numpy as np
import datetime
import json
import math
import re


def etl(df_transactions, df_clients):
    clients_clean = df_clients[df_clients['ClientID'] > 0].copy()
clients_clean = clients_clean.drop_duplicates(subset=['ClientID'], keep='first')
transactions_clean = df_transactions[
    (df_transactions['TransactionID'] > 0) &
    (df_transactions['ClientID'] > 0)
    ].copy()
transactions_clean = transactions_clean.drop_duplicates(subset=['TransactionID'], keep='first')
transactions_clean = transactions_clean[transactions_clean['Date'].str.match(r'^\d{4}-\d{2}-\d{2}$', na=False)]
merged_df = pd.merge(transactions_clean, clients_clean, on='ClientID', how='inner')
merged_df['Amount'] = merged_df['Amount'].astype(int)
columns = [
    'TransactionID',
    'ClientID',
    'Date',
    'Amount',
    'ClientName',
    'Industry'
]
return merged_df[columns]