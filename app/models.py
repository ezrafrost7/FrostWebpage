"""
Definition of models.
"""

from django.db import models
import datetime
from datetime import date

# Create your models here.

class CompanyData(models.Model):

    #data fields/attributes for the model
    StockDate = models.DateField(default=date.today(), blank=True)
    Negative = models.DecimalField(max_digits=4, decimal_places=2)
    Neutral = models.DecimalField(max_digits=4, decimal_places=2)
    Positive = models.DecimalField(max_digits=4, decimal_places=2)
    Compound = models.DecimalField(max_digits=4, decimal_places=2)
    StockOpen = models.DecimalField(max_digits=10, decimal_places=2)
    StockHigh = models.DecimalField(max_digits=10, decimal_places=2)
    StockLow = models.DecimalField(max_digits=10, decimal_places=2)
    StockClose = models.DecimalField(max_digits=10, decimal_places=2)
    CompanyName = models.CharField(max_length=50)
    Ticker = models.CharField(max_length=10)
