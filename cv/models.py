from django.db import models

# Create your models here.
class Education(models.Model):
    title = models.CharField(max_length=200)
    grades = models.CharField(max_length=200)
    description = models.TextField(default=None)
    graduation_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Experience(models.Model):
    title = models.CharField(max_length=200)
    position = models.TextField()
    text = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Skills(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default=None)

    def __str__(self):
        return self.title

class Interests(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
