#import the stock function
from app.models import CompanyData

comps = CompanyData()

companies = [['tesla', 'tsla'], ['apple', 'aapl'], ['delta', 'dal']]
for c in companies:
    comps.runData(c[0], c[1])