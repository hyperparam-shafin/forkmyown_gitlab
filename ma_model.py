 Load data from RDS

    In [10]:
   import pandas as pd
from sqlalchemy import create_engine

db_host = "yieldmanagement.cluster-c2jaydssljuc.us-west-2.rds.amazonaws.com"
db_username = "ymdsmaster"
db_password = ''
db_name = "yieldmanagement"
db_port = 6174
start_date = "2017-11-01"
end_date = "2017-11-01"
prediction_length = 10 

conn = create_engine(f'mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}', echo=False)


df = pd.read_sql(f"select network_number, timeslot, start_date, household_impressions from rentrak_impressions where start_date between '{start_date}' and '{end_date}' and network_number = '9860' and timeslot between 1 and 10 order by network_number, timeslot, start_date;",con=conn)

df['household_impressions']
#   Out [19]:
#   0    2991
#	1    2897
#	2    2767
#	3    2947
#	4    2669
#	5    2294
#	6    1932
#	7    1741
#	8    1357
#	9    1164
#Name: household_impressions, dtype: int64

type(df['start_date'][0]) 
