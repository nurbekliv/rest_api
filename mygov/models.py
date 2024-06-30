from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class Parents(models.Model):
    id = models.AutoField(primary_key=True)
    f_number = models.IntegerField(unique=True)
    m_number = models.IntegerField(unique=True)
    address = models.CharField(max_length=255)


class Children(models.Model):
    ch_number = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    family_id = models.ForeignKey(Parents, on_delete=models.SET_NULL, null=True)
    birth_date = models.DateField()
    foto = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.first_name


class WorkHistory(models.Model):
    work_number = models.ForeignKey(Children, on_delete=models.SET_NULL, null=True)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.company


class Educations(models.Model):
    name = models.CharField(max_length=100)
    education_number = models.ForeignKey(Children, on_delete=models.SET_NULL, null=True)
    start_time = models.DateField()
    end_time = models.DateField()
