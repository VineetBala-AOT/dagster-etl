from dagster import Out, Output, job, op
import logging
from utils.db_con import get_met_app_conn, get_met_analytics_creds
import datetime as dt
#import needed libraries
from sqlalchemy import create_engine
import pandas as pd
import os

#extract data from met app db
@op(out={"df": Out(is_required=True), "tbl": Out(is_required=True)})
def extract_user_data(context):
    try:
        lgr = logging.getLogger('console_logger')
        startTime = str(int(dt.datetime.strptime((dt.datetime.now() - dt.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M'), '%Y-%m-%d %H:%M').timestamp() * 1000))
        endTime = str(int(dt.datetime.strptime(dt.datetime.now().strftime('%Y-%m-%d %H:%M'), '%Y-%m-%d %H:%M').timestamp() * 1000))
        lst = [{1, 'Y', 'tutor@gmail.com', 2, startTime, endTime}]
        df = pd.DataFrame(lst)
        yield Output(df, "df")
        yield Output("user_details1", "tbl")
    except Exception as e:
        print("Data extract error: " + str(e))

#load data to met analytics db
@op
def load_user_data(context, df, tbl):
    engine = create_engine("postgresql://userid:password@localhost:port/database")
    symbols = [1]
    candles = pd.DataFrame()

    for symbol in symbols:
        df['id']=symbol
        df.set_index('id', inplace=True)
        candles = candles.append(df)
    
    candles.to_sql(tbl, con=engine, if_exists='replace')