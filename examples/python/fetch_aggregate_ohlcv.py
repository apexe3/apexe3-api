'''
/**
 * fetch_aggregate_ohlcv.py
 * 
 * Retrieves OHLCV for traditional and digital assets
 * 
 * Disclaimer:
 * APEX:E3 is a financial technology company based in the United Kingdom https://www.apexe3.com
 *  
 * None of this code constitutes financial advice. APEX:E3 is not 
 * liable for any loss resulting from the use of this code or the API. 
 * 
 * This code is governed by The MIT License (MIT)
 * 
 * Copyright (c) 2020 APEX:E3 Team
 * 
 **/
'''

import sys
sys.path.append('..')
from apexe3.apexe3 import initialise
from apexe3.apexe3 import fetch_aggregated_OHLCV

import pandas as pd

def init():
    clientId = "Your-ClientId-Goes-Here"
    clientSecret = "Your-Client-Secret-Goes-Here"
    initialise(clientId, clientSecret)

if __name__ == "__main__":
    init()
    #Change these values to a ticker you are interested in - see the supportedAssetIdsForAggregateOHLCV folder for searchable tickers
    table=pd.DataFrame(fetch_aggregated_OHLCV('YFII-ETH', '2018-01-01','2020-12-31',''))
    
    print(table)