from django.db import models


# Create your models here.
class PhoneNumber(models.Model):
    number = models.CharField(max_length=9)

    def __str__(self):
        return self.number


class Person(models.Model):
    phone_number = models.OneToOneField(
        PhoneNumber,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "People"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
