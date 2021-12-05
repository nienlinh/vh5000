from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns


# Create your models here.


class Prize(models.Model):
    pid = models.CharField(max_length=25)
    cname = models.CharField(max_length=20)
    amount = models.IntegerField()

    def get_url(self):
        return reverse('prize-detail', args=[str(self.id)])

    def __str__(self):
        return self.cname


class Winner(models.Model):
    last_ssn = models.CharField(max_length=3)
    prize_id = models.ForeignKey(
        "Prize", on_delete=models.CASCADE)

    def __str__(self):
        return self.prize_id.cname + ", " + self.last_ssn


