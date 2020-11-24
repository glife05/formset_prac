from django.db import models

# Create your models here.
class Programmer(models.Model):
    name=models.CharField(max_length=20)


    def __str__(self):
        return self.name


class Language(models.Model):
    name=models.CharField(max_length=15)
    programmer=models.ForeignKey(Programmer,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

