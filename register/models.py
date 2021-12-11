from django.db import models


# Create your models here.
class Person(models.Model):

    VOUCHER_CHOICES = [
        ('PP', '紙本'),
        ('CC', '信用卡'),
        ('ET', '電子票劵'),
        ('MB', '行動支付')
    ]
    ssn = models.CharField(max_length=10, blank=False)
    tel = models.CharField(max_length=20, blank=False)
    voucher_id = models.CharField(max_length=2, choices = VOUCHER_CHOICES, default='PP')

    class Meta:
        ordering = ['-ssn']

    def __str__(self):
        return self.ssn
