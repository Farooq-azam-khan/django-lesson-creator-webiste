from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = settings.AUTH_USER_MODEL

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Finance(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))
    balance = models.DecimalField(max_digits=1000000, decimal_places=3)

    def __str__(self):
        return self.owner.username


class StockPurchaseHisotry(models.Model):
    owner = models.ForeignKey(Finance, on_delete=models.CASCADE)
    stock_name = models.CharField(max_length=10)
    time_purchased = models.DateTimeField(auto_now_add=True)
    amout_purchased = models.DecimalField(max_digits=1000000, decimal_places=3)
    hm_purchased = models.IntegerField()

    def __str__(self):
        return self.owner.username

class StockSoldHistory(models.Model):
    owner = models.ForeignKey(Finance, on_delete=models.CASCADE)
    stock_name = models.CharField(max_length=10)
    time_sold = models.DateTimeField(auto_now_add=True)
    amout_sold = models.DecimalField(max_digits=1000000, decimal_places=3)
    hm_sold = models.IntegerField()

    def __str__(self):
        return self.owner.username
