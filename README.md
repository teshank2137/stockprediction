# Stock Prediction API
**Flask API**

A SVM model hosted with Flask to predict next days closing price of a Particular Stock

![banner](https://github.com/teshank2137/stockprediction/blob/main/media/ss.JPG?raw=true)
*StartUp page*

###How To get Stockname
- Open [Yahoo Finance ](https://finance.yahoo.com/) and select get the Stock's Symbol from there
- Replace *[stockname]* with your stock symbol in the following endpoints
---
##Endpoints
**To get buy sell hold flag for today**
`GET https://baseurl/predict/[stockname]`
**To get list of Stocks**
`GET https://baseurl/stock`
**To get Current Market price of stock**
`GET https://baseurl/current/[stockname]`
**To get previous 1 week data of a stock**
`GET https://baseurl/week/[stockname]`
**To get tomorrow's closing price prediction**
`GET https://baseurl/rawpredict/[stockname]`
**To get full data of previous `n` days included moving average of a stock**
`GET https://baseurl/[stockname]/[n]`

---