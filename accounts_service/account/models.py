from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)

    def serialize(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname
        }
