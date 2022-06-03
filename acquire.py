import pandas as pd
import numpy as np
from env import get_db_url
import os

def get_zillow_data():
    filename = 'zillow.csv'
    
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    
    else:
        sql = '''
        SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, fips, assessmentyear, landtaxvaluedollarcnt, lotsizesquarefeet, latitude, longitude
        FROM properties_2017
        WHERE propertylandusetypeid = 261;
        '''

        df = pd.read_sql(sql, get_db_url('zillow'))

        df.to_csv(filename)

        return df 

def get_zillow_locs():
    filename = 'zillowloc.csv'

    if os.path.isfile(filename):
        return pd.read_csv(filename)

    else:
        sql = '''
        SELECT parcelid, latitude, longitude
        FROM properties_2017
        WHERE propertylandusetypeid = 261;
        '''

        df = pd.read_sql(sql, get_db_url('zillow'))

        df.to_csv(filename)

        return df 




