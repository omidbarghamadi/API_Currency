from django.db import models
from datetime import datetime, time
# Create your models here.


class currency(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField()
    date = models.DateField(auto_now=True)
    time = models.TimeField(default=datetime.now().time())
