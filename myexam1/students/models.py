from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    id =models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name

