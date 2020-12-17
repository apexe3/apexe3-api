'''
/**
 * run_backtest.py
 * 
 * Runs a backtest based on supplied parameters
 * Read more here: https://intercom.help/apexe3/en/articles/4711970-programmatic-backtesing
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
from apexe3.apexe3 import run_backtest
import json

import pandas as pd

def init():
    clientId = "your-client-id-goes-here"
    clientSecret = "your-client-secret-goes-here"
    initialise(clientId, clientSecret)

if __name__ == "__main__":
    init()
    
    #Read about how to use this API here:
    #https://intercom.help/apexe3/en/articles/4711970-programmatic-backtesing
    

    indicatorParams = {

        'indicator1': {
            'type': 'rsi',
            'period':'14'
        },

        'indicator2': {
            'type':'macd',
            'shortPeriod': '12',
            'longPeriod': '26',
            'signalPeriod': '9',
        }

    }




    multiStrategyParams = {

        'longEntryIndicator1': 'hour',
        'longEntryOperator': '==',
        'longEntryIndicator2': '12',

        'shortEntryIndicator1': 'hour',
        'shortEntryOperator': '==',
        'shortEntryIndicator2': '22',


        'longExitIndicator1': 'hour',
        'longExitOperator': '==',
        'longExitIndicator2': '5',

        'shortExitIndicator1': 'hour',
        'shortExitOperator': '==',
        'shortExitIndicator2': '20',

        'stopLoss': '6',

    }

    
    result = run_backtest('10000', 'COINBASEPRO', 'BTC', 'USD', '01-07-2017', '31-12-2020', indicatorParams, multiStrategyParams,'1h', 'true')
    
    print(result['analysis'])

    #table=pd.DataFrame(result['trades'])
    #table=pd.DataFrame(result['marketData'])
    #print(table)
