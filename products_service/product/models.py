from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    weight = models.IntegerField()

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "weight": self.weight
        }
