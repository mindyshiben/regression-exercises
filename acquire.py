import pandas as pd
import numpy as np
from env import get_db_url

def get_zillow_data():
    sql = '''
    SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, fips
    FROM properties_2017
    WHERE propertylandusetypeid = 261;
    '''
    df = pd.read_sql(sql, get_db_url('zillow'))
    return df 