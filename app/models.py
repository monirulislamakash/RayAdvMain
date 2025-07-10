from django.db import models
from tinymce import models as tinymce_models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Gallery(models.Model):
    image=models.FileField(upload_to="media/GalleryImage/")
class TrafficPartners(models.Model):
    image=models.FileField(upload_to="media/TraficImage/")
class FeaturedIn(models.Model):
    image=models.FileField(upload_to="media/FeaturedImage/")
class FrequentlyAskedQuestions(models.Model):
    Question=models.CharField(max_length=200)
    Answer=models.TextField()
    def __str__(self):
        return self.Question
class ProudlySponsoring(models.Model):
    Icon=models.FileField(upload_to="media/TraficImage/")
    Titel=models.CharField(max_length=100)
    Description=models.TextField()
    ButtonLink=models.CharField(max_length=100)
    def __str__(self):
        return self.Titel

class EventCategory(models.Model):
    category=models.CharField(max_length=100)
    def __str__(self):
        return self.category
class BlogCategory(models.Model):
    category=models.CharField(max_length=100)
    def __str__(self):
        return self.category
class Event(models.Model):
    Titel=models.CharField(max_length=100)
    category=models.ForeignKey(EventCategory,on_delete=models.CASCADE)
    Images=models.FileField(upload_to="media/Event/")
    Thumbnail=models.FileField(upload_to="media/Event/")
    Body=tinymce_models.HTMLField()
    PostDate=models.CharField(max_length=100)
    Location=models.CharField(max_length=100)
    def __str__(self):
        return self.Titel

class Blog(models.Model):
    Titel=models.CharField(max_length=100)
    category=models.ForeignKey(BlogCategory,on_delete=models.CASCADE)
    Images=models.FileField(upload_to="media/Blog/")
    Body=tinymce_models.HTMLField()
    PostDate=models.DateField(default=datetime.datetime.today())
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.Titel
    
class CareersCategory(models.Model):
    category=models.CharField(max_length=100)
    def __str__(self):
        return self.category
    
class Career(models.Model):
    Titel=models.CharField(max_length=100)
    vacancy=models.CharField(max_length=100)
    Experience=models.CharField(max_length=100)
    Location=models.CharField(max_length=100)
    JobType=models.CharField(max_length=100)
    SalaryRange=models.CharField(max_length=100)  
    category=models.ForeignKey(CareersCategory,on_delete=models.CASCADE)
    PostDate=models.DateField(default=datetime.datetime.today())
    description=tinymce_models.HTMLField()
    
class AppliedCandidates(models.Model):
    Position=models.CharField(max_length=100)
    Name=models.CharField(max_length=100)
    Phone=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    CV=models.FileField(upload_to="media/CandidatesCV/")
    Cover_Letter=models.TextField()

class PrivacyPolicy(models.Model):
    Privacy_Policy=tinymce_models.HTMLField()
    Last_Update=models.DateField(default=datetime.datetime.today())

class TermsAndConditions(models.Model):
    Terms_Conditions=tinymce_models.HTMLField()
    Last_Update=models.DateField(default=datetime.datetime.today())

class Disclaimer(models.Model):
    Terms_Conditions=tinymce_models.HTMLField()
    Last_Update=models.DateField(default=datetime.datetime.today())