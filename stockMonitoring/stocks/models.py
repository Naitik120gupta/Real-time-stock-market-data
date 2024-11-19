from django.db import models
class StockPrice(models.Model):
    stock_name = models.CharField(max_length=50)
    price = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.stock_name} - ${self.price} at {self.timestamp}"
