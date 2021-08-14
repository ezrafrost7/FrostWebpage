def runData(companyName, ticker, crypto=False) :
    #dependencies to be imported

    import pandas as pd
    import nltk
    from nltk.sentiment import SentimentIntensityAnalyzer
    import requests
    import json
    import datetime
    import sqlite3
    from app.models import CompanyData
    from bs4 import BeautifulSoup

    #the api keys and other universal veriables/objects

    newsApiKey = '481ab4f4d4fd4861aa48dedcdc645900'
    #extractorApiKey = '54476f1dd1c4db5b381ea9e306cfd21d2ac65da3'
    stockApiKey = 'c3o3oc2ad3ia07uekun0'
    sia = SentimentIntensityAnalyzer()
    today = datetime.date.today()
    companyName = companyName.upper()
    ticker = ticker.upper()
    article = ""

    #creating new CompayData object
    Company = CompanyData()

    #creating the api request url for the newsapi
    #returns the list of news articles that we use for the url

    url = f'https://newsapi.org/v2/top-headlines?q={companyName}&from={today}&to={today}&sortBy=popularity&apiKey={newsApiKey}&category=business&pageSize=10'
    req = requests.get(url)

    #generating the JSON object that is returned from the request

    response = json.loads(req.text)

    #extracting all of the article text and appending it into an array

    for r in response['articles']:
        articleReq = requests.get(f'{r["url"]}')
        try:
            soup = BeautifulSoup(articleReq.content, 'html.parser')
            for tag in soup.body.find_all('p'):
                article += tag.text
        except:
            pass
    
    content = article.split('.')

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
                row.append(sia.polarity_scores(c)[col])
            except:
                row.append(None)
        dailyDf.loc[r] = row
        r += 1
    
    #retrieving financial stock data

    stockReq = requests.get(f'https://finnhub.io/api/v1/quote?symbol={ticker}&token={stockApiKey}')
    stockJson = stockReq.json()

    #create object and save the data to the object
        
    Company.Negative = dailyDf['neg'].mean()
    Company.Neutral = dailyDf['neu'].mean()
    Company.Positive = dailyDf['pos'].mean()
    Company.Compound = dailyDf['compound'].mean()
    Company.StockDate = today
    Company.CompanyName = companyName
    Company.Ticker = ticker
    Company.StockOpen = stockJson['o']
    Company.StockHigh = stockJson['h']
    Company.StockLow = stockJson['l']
    Company.StockClose = stockJson['pc']

    #saving the company data to the DB
    Company.save()


#this function will run to update the graphs that are displayed on the webpage
def Graphics(companyName):

    #imports
    from .models import CompanyData
    import pandas
    from matplotlib import pyplot as plt
    import seaborn as sns
    import sqlite3

    #make connection
    conn = sqlite3.connect("db.sqlite3")

    #make query into a pandas df
    df = pandas.read_sql_query(f'SELECT * from app_companydata WHERE CompanyName == "{companyName.upper()}"', conn)

    #always close connection
    conn.close()

    #start plotting using the dataframe that we have just saved
    ax = plt.subplot()
    ln1 = ax.plot(df['StockDate'], df['Compound'], 'ro', label='Sentiment Score')
    ax.tick_params(axis='y', labelcolor='red')
    ax.set_ylabel('Sentiment Score')
    ax.set_xlabel('Date')
    ax.set_title(f'{companyName.upper()}')
    ax.axhline(color='gray', linestyle='--')

    ax2 = ax.twinx()

    ln2 = ax2.plot(df['StockDate'], df['StockOpen'], 'b', label= 'Open Price')
    ln3 = ax2.plot(df['StockDate'], df['StockClose'], 'b--', label= 'Close Price')
    ax2.tick_params(axis='y', labelcolor='blue')
    ax2.set_ylabel('Stock Price ($)')
    lns = ln1+ln2+ln3
    labs = [l.get_label() for l in lns]
    ax2.legend(lns, labs)

    plt.savefig(f'.\\app\\static\\app\\img\\{companyName.upper()}.png')

    #clear out the figure
    plt.clf()


#this is the function that will be set to run everyday in order to grab data from the interwebs
def RunModules():

    #imports and needed variable
    
    from .models import CompanyData

    print("starting apis")

    comps = CompanyData()
    companies = [['tesla', 'tsla'], ['apple', 'aapl'], ['delta', 'dal'],['microsoft','msft'],['amc','amc']]

    for c in companies:
        print("start")
        runData(c[0], c[1])
        print("end")

    for c in companies:
        Graphics(c[0])