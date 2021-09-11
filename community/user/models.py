from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(
        max_length=64,
        verbose_name='username'
    )

    password = models.CharField(
        max_length=64,
        verbose_name='password'
    )

    registered_dttm = models.DateTimeField(
        auto_now_add=True,
        verbose_name='registered_date'
    )

    class Meta:
        db_table ='user'


       