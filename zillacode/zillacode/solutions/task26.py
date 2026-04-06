def etl(df):
	extracted_pct = df['Description'].str.extract(r'\[(\d+)%\s*off\]', expand=False)
    df['Discount'] = (extracted_pct.astype(float) / 100).fillna(0.0)
    columns = [
        'StoreID',
        'ProductName',
        'Category',
        'SoldUnits',
        'Description',
        'Discount'
    ]
    return df[columns]