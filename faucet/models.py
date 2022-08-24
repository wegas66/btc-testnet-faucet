from django.db import models


class Address(models.Model):
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.address


class Transaction(models.Model):
    hash_str = models.TextField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    value = models.IntegerField(default=10000)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hash_str
