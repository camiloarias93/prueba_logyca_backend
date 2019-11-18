from django.db import models

class Student(models.Model):
    name  = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name

class Professor(models.Model):
    name  = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name

class Score(models.Model):
    name  = models.CharField(max_length=100, blank=False, null=False)
    value = models.IntegerField(blank=False, null=False)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

