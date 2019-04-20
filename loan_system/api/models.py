from django.db import models


class Loan(models.Model):
    loan_id = models.CharField(max_length=18, default=None)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    rate = models.DecimalField(max_digits=3, decimal_places=2)
    date_start = models.DateField()
    date_end = models.DateField()


    def __str__(self):
        return "{}".format(self.id)

class Payment(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=4)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    rate = models.DecimalField(max_digits=3, decimal_places=2)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "{} - {}".format(self.type, self.amount)