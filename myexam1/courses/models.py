from django.db import models
from students.models import Student



class Course(models.Model):
    name = models.CharField(max_length=50)
    course_id = models.IntegerField(null=False)

    def __str__(self):
        return self.name


class Class101(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.course.name + " - " + self.student.name