# APEX:E3 - API Nodejs Low Code Examples

![preview](https://github.com/apexe3/apexe3-api/blob/main/examples/nodejs/apexe3/assets/nodejsondemandscreener.png?raw=true)

All examples make use of the apexe3/apexe3.js wrapper which implements a subset of the REST and websocket API definitions defined in the [APEX:E3 API documentation](https://api.ae3platform.com/docs). 

## Real-time Global Orderbook

Access the Real-time Global Orderbook for any asset Pair across any exchanges.

To run: 

```shell
cd apexe3-api/examples/nodejs
node real-time-global-orderbook.js
```
This will output the global orderbooks for bids and asks, by best bid and ask prices respectively (only bids are shown in the picture below for the sake of example).

![preview](https://github.com/apexe3/apexe3-api/blob/main/examples/nodejs/apexe3/assets/nodejsglobalorderbook.png?raw=true)

**As the picture above shows, the top 25 depth for BTC/USDT is taken from each exchange, combined and ordered to produce a globally updating orderbook ready for real-time algorithmic trading or analysis.** 

The initialiseGlobalOrderbook function initialises the global orderbook with BTC/USDT SPOT market. You can change the pair as desired. (Derivatives (SWAP, FUTURE) are also supported).
```javascript
   await apexe3.initialiseGlobalOrderbook(base,quote);
```

In this example, the following columns **are retrieved for every BTC/USDT orderbook update across supported exchanges in real-time.**

- bid price (bid px) (ordered by best bid across exchanges).
- bid size 
- cumulative bid size (bid size added up at each depth)
- bid sum (bid px * bid size)
- cumulative bid sum are retrieved (bid sum added up at each depth)
- exchange

All updates are emitted and converted to an easily processable data structure for further programmatic analysis.

You can easily access the structured data as it updates in the streams callback function.

```javascript
    stream.on('GLOBAL_ORDERBOOK', (globalOrderbook) => { /** do stuff here **/ });
```
You can easily process the globalOrderbook of bids (or asks) in your trading algorithm logic, store it for historical analysis or manipulate as desired.

## Real-time Global Liquidity

Access the Real-time total supply & demand of Liquidity for any asset pair across any exchange.

To run: 

```shell
cd apexe3-api/examples/nodejs
node real-time-liquidity.js
```

This will output the total demand (bid) and supply (ask) liquidity for the BTC/USDT Spot market. 
![preview](https://github.com/apexe3/apexe3-api/blob/main/examples/nodejs/apexe3/assets/nodejsgloballiquidity.png?raw=true)

The above picture shows a real-time aggregation of the top 25 depth of BTC/USDT Spot markets across supported exchanges. 
In this example, the following columns **are retrieved for every BTC/USDT orderbook update across supported exchanges in real-time.**

- Exchange
- Ask Liqudity (The total USDT amount available to buy on the relevant exchange at that moment in time. This is based on the top 25 depth)
- Bid Liqudity (The total USDT in demand on the relevant exchange at that moment in time. This is based on the top 25 depth)
- Amount (The amount of BTC available to buy on the relevant exchange at that moment in time. This is based on the top 25 depth)
- Imbalance (Ask Liquidity - Bid Liquidity)
- Market Price_25 (The likely price of a market order filling the top 25 orders on that exchange)


All updates are emitted and converted to structured data for further programmatic analysis.

You can easily access the structured data as it updates in real-time in the process_global_orderbook function.
```javascript
    stream.on('LIVE_LIQUIDITY', (globalLiquidity) => { /** do stuff here **/  });
```
**You can easily process this data in your trading algorithm, smart order routing logic, store it for historical analysis or manipulate as desired.**

## Real-time Insights
 
Identify whale prders, arbitrage opportunities, large/medium/small Bid/Ask imbalances & tightest spreads for any asset pair across any exchange.

To run:

```shell
cd apexe3-api/examples/nodejs
node real-time-insights.js
```
This will output ranked-by-exchange spread, whale and bid/ask imbalances BTC/USD. It will also output ranked arbitrage opportunities for pairs that can be arbitraged across 2 exchanges.

The following example output shows how arbitrages will look in the output.

![preview](https://github.com/apexe3/apexe3-api/blob/main/examples/nodejs/apexe3/assets/nodejsarbs.png?raw=true)


**You can easily process this data in your trading algorithm, or store them to analyse how orderbook whales, spreads, imbalances and arbitrage opportunities evolve over time**

## On-demand Screener

Programmatically screen markets using technical indicators for any asset pair, quote or any exchange.

To run:

```shell
cd apexe3-api/examples/nodejs
node on-demand-screener.js
```
This will output screened results for BTC/USDT consisting of price and volume metrics on an on-demand basis.

![preview](https://github.com/apexe3/apexe3-api/blob/main/examples/nodejs/apexe3/assets/nodejsondemandscreener.png?raw=true)

This example screens the BTC/USDT pair using the following code:

```javascript
    const stats = await screenPair('BTC','USDT');
    console.table(stats, ['exchangeId','baseId', 'quoteId', 'v24HrChg','v30dChg','v24HrVsV30dSum','p15MinChg','p1HrChg','p7dChg','pLast']);
```

A successful response will consist of the following columns:

- exchangeId
- baseId 
- quoteId
- v24HrChange (24 hour volume change)
- v30dChg (30 day volume change)
- v24HrVsV30dSum (24 hour vs 30 day volume change)
- p15MinChg (15 minute price change)
- p1HrChg (1 hour price change)
- p7dChg (7 day price change)
- pLast (latest price)

The screen function, imported from the apexe3.js wrapper class, can take more parameters as follows:

```javascript
    screen(base,quote,exchanges=[], rsi=[],smaCross=[],volatility=[], weeklyOpenChg=[], bollingerBand='', fibRetracements=[], trends=[], ichimoku=[]);
```
This allows for instantly screening pairs, markets or exchanges by RSI, Moving Average, Volatility, Bollinger Bands, Fibretracement, Trends and Ichimoku cloud technical indicator analysis.

Example values for these parameters can be found in apexe3.js under the following section:

```javacript
//screener filter values for reference
```
