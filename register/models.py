from django.db import models


# Create your models here.
class Person(models.Model):
    ssn = models.CharField(max_length=10)
    tel = models.CharField(max_length=20)
    voucher_id = models.ForeignKey(
        "Voucher", on_delete=models.CASCADE)

    class Meta:
        ordering = ['-ssn']

    def __str__(self):
        return self.ssn


class Voucher(models.Model):
    vType = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=0, default=5000)  # max_digits:最大位數,decimal_places:最大位數

    def __str__(self):
        return self.vType
