from django.db import models

# Create your models here.


class Subjects(models.Model):
    tamil = models.IntegerField()
    telugu = models.IntegerField()
    english = models.IntegerField()
    maths = models.IntegerField()
    science = models.IntegerField()
    social = models.IntegerField()


class Staff(models.Model):
    staff_name = models.CharField(max_length=50)
    classes = models.ManyToManyField(Subjects)

    def __str__(self):
        return self.staff_name


class Students(models.Model):
    subjects = models.OneToOneField(Subjects)
    student_name = models.CharField(max_length=50)
    year_of_class = models.IntegerField()

    def __str__(self):
        return self.student_name
