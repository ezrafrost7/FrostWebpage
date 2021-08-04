def runData(companyData, companyName, ticker, crypto=False) :
    #dependencies to be imported

    import pandas as pd
    import nltk
    from nltk.sentiment import SentimentIntensityAnalyzer
    import requests
    import json
    import datetime
    import sqlite3
    from app.models import CompanyData

    #the api keys and other universal veriables/objects

    newsApiKey = '481ab4f4d4fd4861aa48dedcdc645900'
    extractorApiKey = '54476f1dd1c4db5b381ea9e306cfd21d2ac65da3'
    stockApiKey = 'c3o3oc2ad3ia07uekun0'
    sia = SentimentIntensityAnalyzer()
    today = datetime.date.today()
    companyName = companyName.upper()
    ticker = ticker.upper()

    #creating new CompayData object
    #Company = CompanyData()

    #creating the api request url for the newsapi
    #returns the list of news articles that we use for the url

    url = f'https://newsapi.org/v2/top-headlines?q={companyName}&from={today}&to={today}&sortBy=popularity&apiKey={newsApiKey}&category=business&pageSize=10'
    req = requests.get(url)

    #generating the JSON object that is returned from the request

    response = json.loads(req.text)

    #extracting all of the article text and appending it into an array

    content = []
    for r in response['articles']:
        extractorReq = requests.get(f'https://extractorapi.com/api/v1/extractor/?apikey={extractorApiKey}&url={r["url"]}')
        try:
            content.append(json.loads(extractorReq.text))
        except:
            pass
    
    #running polarity scores of each of the articles
    #this might need to be modified, the polarity scores are more accurate with smaller texts
    #and the article texts can be pretty long
    #this is also loading that information into a pandas DF

    dailyDf = pd.DataFrame(columns=['neg','neu','pos','compound'])
    r = 0
    for c in content:
        row = []
        for col in dailyDf:
            try:
                row.append(sia.polarity_scores(c['text'])[col])
            except:
                row.append(None)
        dailyDf.loc[r] = row
        r += 1
    
    #retrieving financial stock data

    stockReq = requests.get(f'https://finnhub.io/api/v1/quote?symbol={ticker}&token={stockApiKey}')
    stockJson = stockReq.json()

    #create object and save the data to the object
        
    companyData.Negative = dailyDf['neg'].mean()
    companyData.Neutral = dailyDf['neu'].mean()
    companyData.Positive = dailyDf['pos'].mean()
    companyData.Compound = dailyDf['compound'].mean()
    companyData.StockDate = today
    companyData.CompanyName = companyName
    companyData.Ticker = ticker
    companyData.StockOpen = stockJson['o']
    companyData.StockHigh = stockJson['h']
    companyData.StockLow = stockJson['l']
    companyData.StockClose = stockJson['pc']

    #saving the company data to the DB
    companyData.save()

#this is the function that will be set to run everyday in order to grab data from the interwebs
def FinModule():

    #imports and needed variable
    
    from .models import CompanyData

    print("starting apis")

    comps = CompanyData()
    companies = [['tesla', 'tsla'], ['apple', 'aapl'], ['delta', 'dal']]

    for c in companies:
        print("start")
        runData(comps, c[0], c[1])
        print("end")