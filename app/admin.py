#added admin file for the application

from django.contrib import admin
from .models import CompanyData

#registering the models to be viewed on the site
admin.site.register(CompanyData)