from django.db import models
from django.urls import reverse

# Create your models here.
class departments(models.Model):

    department_name=models.CharField(max_length=100)

    def __str__(self):
        return self.department_name

class institutes(models.Model):

    department=models.ForeignKey("departments",on_delete=models.CASCADE)
    institute_name=models.CharField(max_length=100)
    def __str__(self):
        return self.institute_name


class thesis_listings (models.Model):
    Eng = "English"
    Ger = "German"
    LANGUAGE_CHOICES = (
        (Eng, "English"),
        (Ger, "German"),
    )
    Bachelor= "Bachelor"
    Master="Master"
    PhD="Phd"
    All_levels ="Open to all levels"
    STUDENT_LEVEL= (
        (Bachelor, "Bachelor"),
        (Master, "Master"),
        (PhD, "Phd"),
        (All_levels, "Open to all levels"),
    )
    

    supervisor=models.CharField(max_length=30)
    title = models.CharField(max_length =100)
    description = models.TextField (max_length = 1000)
    creation_date = models.DateField(auto_now_add=True, blank=True)
    writing_language = models.CharField(choices = LANGUAGE_CHOICES)
    department=models.ForeignKey("departments",on_delete=models.CASCADE)
    institute=models.ForeignKey("institutes",on_delete=models.CASCADE)
    student_level = models.CharField(choices = STUDENT_LEVEL)
    Degree_program = models.SmallIntegerField
    accompanying_file = models.FileField(upload_to=None, max_length=254,blank=True)
    additional_information = models.CharField(max_length = 100,blank=True)
    contact = models.CharField(max_length = 100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ('studentforum:post_view',kwargs={'pk':self.pk})


