from django.db import models

# Create your models here.
class morning(models.Model):
    slot1=models.CharField(max_length=60)
    occupied = models.BooleanField()

    def __str__(self):
        return self.slot1

    def get_id(self):
        return self.id

class afternoon(models.Model):
    slot2=models.CharField(max_length=60)
    occupied = models.BooleanField()

    def __str__(self):
        return self.slot2

    def get_id(self):
        return self.id

class evening(models.Model):
    slot3=models.CharField(max_length=60)
    occupied = models.BooleanField()

    def __str__(self):
        return self.slot3

    def get_id(self):
        return self.id

class employee(models.Model):
    username=models.CharField(max_length=60)
    password=models.CharField(max_length=60)
    name=models.CharField(max_length=60)

    def __str__(self):
        return self.name

    def get_id(self):
        return self.id

