from django.db import models

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=50)
    story = models.TextField()
    score = models.IntegerField(default=0)

    def __str__(self):
	    return self.title


class Question(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    question = models.TextField(unique = True)
    choice_one = models.CharField(max_length=50)
    choice_two = models.CharField(max_length=50)
    choice_three = models.CharField(max_length=50)
    choice_four = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)
    

