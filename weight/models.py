from django.db import models
from django.contrib.auth.models import User


class Weight(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=4, decimal_places=1)
    date = models.DateField()

    def __str__(self):
        return str(self.date) + ' ' + str(self.username)