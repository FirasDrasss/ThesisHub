from django.db import models
from django.urls import reverse

# Create your models here.


class post (models.Model):
    Eng = "English"
    Ger = "German"
    LANGUAGE_CHOICES = (
        (Eng, "English"),
        (Ger, "German"),
    )
    author=models.CharField(max_length=30)
    title = models.CharField(max_length = 100)
    description = models.TextField (max_length = 1000)
    creation_date = models.DateField(auto_now_add=True, blank=True)
    writing_language = models.CharField(choices = LANGUAGE_CHOICES)
    additional_information = models.CharField(max_length = 100,blank=True)
    contact = models.CharField(max_length = 100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ('studentforum:post_view',kwargs={'pk':self.pk})