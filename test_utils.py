import pandas as pd
import numpy as np
from sklearn.preprocessing import scale
import pytest
import utils.utils as utils

@pytest.fixture
def clean_df():
    df=pd.DataFrame()
    df['bnk_revlvng_trds_num'] = [5]
    df['curr_bal'] = [3]
    df['avg_bill'] = [9]
    df['core_programming'] = ['KNOWN']
    df['all_star'] = ['KNOWN']
    df['payment_method'] = ['KNOWN']
    df['line_of_business'] = ['KNOWN']
    df['prime_post_office_name'] = ['KNOWN']
    return df

@pytest.fixture
def df_with_nas():
    df=pd.DataFrame()
    df['bnk_revlvng_trds_num'] = [5,np.nan,4,3]
    df['curr_bal'] = [3,1,1,1]
    df['avg_bill'] = [9,1,1,1]
    df['core_programming'] = ['KNOWN',1,1,1]
    df['all_star'] = ['KNOWN',1,1,1]
    df['payment_method'] = ['KNOWN',1,1,1]
    df['line_of_business'] = ['KNOWN',1,1,1]
    df['prime_post_office_name'] = ['KNOWN',1,1,1]
    return df


def test_impute_clean_data(clean_df,):
    df=utils.impute(clean_df)
    assert df['bnk_revlvng_trds_num'].values == ([5])
    assert df['curr_bal'].values == 3
    assert df['avg_bill'].values == 9
    assert df['core_programming'].values == 'KNOWN'
    assert df['all_star'].values == 'KNOWN'
    assert df['payment_method'].values == 'KNOWN'
    assert df['line_of_business'].values == 'KNOWN'
    assert df['prime_post_office_name'].values == 'KNOWN'

def test_impute_bad_data(df_with_nas):
    df=utils.impute(df_with_nas)
    assert df['bnk_revlvng_trds_num'].values == ([5.0,4.0,4.0,3.0])
