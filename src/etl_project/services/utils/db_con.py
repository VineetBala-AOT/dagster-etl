import os
from sqlalchemy import create_engine

#

def get_met_app_conn():
    #get password from environmnet var
    pwd = os.getenv("MET_DB_PASSWORD", "")
    uid = os.getenv("MET_DB_USER", "")
    #
    server = os.getenv("MET_DB_HOST", "")
    db =  os.getenv("MET_DB_DB", "")
    uid = uid
    pwd = pwd
    port = int(os.getenv("MET_DB_PORT", 54332))
    appdbconn = create_engine(f'postgres://{uid}:{pwd}@{server}:{port}/{db}')
    try:
        return appdbconn
    except:
        print("Error loading the config file.")


def get_met_analytics_creds():
    #get password from environmnet var
    pwd = os.getenv("MET_ANALYTICS_DB_PASSWORD", "")
    uid = os.getenv("MET_ANALYTICS_DB_USER", "")
    #
    server = os.getenv("MET_ANALYTICS_DB_HOST", "")
    db =  os.getenv("MET_ANALYTICS_DB_DB", "")
    uid = uid
    pwd = pwd
    port = int(os.getenv("MET_ANALYTICS_DB_PORT", 54334))
    analyticsdbconn = create_engine(f'postgres://{uid}:{pwd}@{server}:{port}/{db}')
    try:
        return analyticsdbconn
    except:
        print("Error loading the config file.")