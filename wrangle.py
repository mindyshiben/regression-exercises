import pandas as pd
import numpy as np
from env import get_db_url
import acquire 

def wrangle_zillow(df):
    df = df.dropna()
    df.rename(columns={'bedroomcnt': 'bedrooms', 'bathroomcnt': 'bathrooms', 'calculatedfinishedsquarefeet': 'square_feet', 'taxvaluedollarcnt': 'value', 'yearbuilt': 'year', 'taxamount': 'tax'}, inplace=True)
    df = df[df.bathrooms != 0]
    df = df[df.bathrooms != 1.75]
    df= df[df.bathrooms < 8]
    df = df[df.square_feet > 200]
    df = df[df.bedrooms != 0.0]
    df = df[df.bedrooms < 8.0]
    df = df[df.value > 200.0]
    df = df[df.value < 8000000.0]
    df['year'] = df['year'].astype('int')
    df['fips'] = df['fips'].astype('int')
    df['square_feet'] = df['square_feet'].astype('int')
    df['value'] = df['value'].astype('int')
    df['county'] = df['fips'].replace({6037: 'los_angeles', 6059: 'orange', 6111: 'ventura'})
    
    return df
    