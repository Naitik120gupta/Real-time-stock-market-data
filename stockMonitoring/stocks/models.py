from django.db import models
class StockPrice(models.Model):
    stock_symbol = models.CharField(max_length=10)
    price = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.stock_symbol} - ${self.price} at {self.timestamp}"
