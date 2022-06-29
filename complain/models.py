from msilib.schema import RadioButton
from typing_extensions import Required
from django.db import models
from django.urls import reverse

PERSON_CHOICES=(
    ('Student','Student'),
    ('Staff','Staff'),
    ('Visitor','Visitor'),
    ('Parent','Parent')
)

title_choice = (
    ('Harasment','Harasment'),
    ('Misconduct', 'Misconduct'),
    ('Cultism','Cultism'),
    ('Extortion','Extortion'),
    ('Dressing','Dressing'),
    ('School Environment','School Environment'),
    ('Others','Others'),
)

class Complain(models.Model):
   
    title = models.CharField(max_length=40, choices=title_choice)
    #author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    person = models.CharField(max_length=25,
        choices=PERSON_CHOICES, default='Student')
   
    treated = models.BooleanField(default=False)
    #evidence = models.FieldFile()

    class Meta:
        ordering = ['-date_added',]
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("thanks")


class Bug(models.Model):
    describe_bug = models.TextField()

    def __str__(self):
        return self.describe_bug
