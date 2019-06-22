from django.db import models



class customers(models.Model):

    email=models.CharField('email', max_length=255)
    username=models.CharField('username', max_length=255)
    password=models.CharField('pass', max_length=255)
    active=models.CharField('active', max_length=10)

class employees(models.Model):
    username=models.CharField('username', max_length=255)
    email=models.CharField('email', max_length=255)
    type=models.CharField('type', max_length=255)
    password=models.CharField('pass', max_length=10)
    def __str__(self):
        return self.email


class services(models.Model):

    email_employees=models.CharField("email_employees", max_length=255)
    email_customers=models.CharField("email_customers", max_length=255)
    name_service=models.CharField('name_service', max_length=255)
    active=models.CharField('active', max_length=10)


