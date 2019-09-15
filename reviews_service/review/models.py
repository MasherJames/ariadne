from django.db import models

# Create your models here.


class Review(models.Model):
    content = models.CharField(max_length=100)

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content
        }
