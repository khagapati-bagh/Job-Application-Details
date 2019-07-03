from django.db import models

# Create your models here.

class Company(models.Model):
    c_name = models.CharField(max_length=30)
    c_link = models.CharField(max_length=200)

    def __str__(self):
        return self.c_name

class Application(models.Model):
    c_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)#Description
    feedback = models.CharField(max_length=100)
    date = models.CharField(max_length=20)
    resume = models.FileField()

    def __str__(self):
        return str(self.c_name) + ' :: '+ self.profile_name



