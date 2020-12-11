/**
 * fetch-aggregate-ohlcv.js
 * 
 * Retrieves market cap OHLCV for digital assets
 * 
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
const apexe3 = require('./apexe3/apexe3');
const cTable = require('console.table');

const clientId = "Your-ClientId-Goes-Here";
const clientSecret = "Your-Client-Secret-Goes-Here";

(async () => {
   
    await apexe3.initialise(clientId, clientSecret);
    //Change these values to a ticker you are interested in -see the supportedAssetIdsForAggregateOHLCV folder for searchable tickers
    let ohlcv = await apexe3.fetchMarketCapForCryptoSymbol('BTC', '01-01-2018','31-12-2020');
   
    console.table(ohlcv.result);
   

})();