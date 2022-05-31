import pandas as pd
import numpy as np
from env import get_db_url

def wrangle_zillow(df):
    df = df.dropna()
    df.rename(columns={'bedroomcnt': 'bedrooms', 'bathroomcnt': 'bathrooms', 'calculatedfinishedsquarefeet': 'square_feet', 'taxvaluedollarcnt': 'value', 'yearbuilt': 'year', 'taxamount': 'tax'}, inplace=True)
    return df