from django.db import models

class FlightListingCollection(models.Model):
    updated_time = models.DateTimeField(auto_now_add=True)
    data = models.TextField(max_length=10000000)
   

class FlightListingCollection2(models.Model):
    updated_time = models.DateTimeField(auto_now_add=True)
    details_data = models.TextField(max_length=10000000)