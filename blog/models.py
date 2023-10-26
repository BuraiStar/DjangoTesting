from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.utils import timezone
import os
import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
def filePathImage(request, filename):
    old_fileName = filename
    timeNow = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    filename = "%s%s" % (timeNow,old_fileName)
    return os.path.join("public/images/",filename)

def filePathFile(request, filename):
    old_fileName = filename
    timeNow = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    filename = "%s%s" % (timeNow,old_fileName)
    return os.path.join("public/images/",filename)
    
class Post(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="published")
        
    options = (("draft", "Draft"), ("published", "Published"))
    
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content =  models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date="published")
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    status = models.CharField(max_length= 10, choices=options, default="published")
    
    objects = models.Manager()
    postObjects = PostObjects()
    
    class Meta:
        ordering = ("-published",)
        
    def __str__(self):
        return self.title
    
class Carousel(models.Model):
    class CarouselObjects(models.Manager):
        def get_queryset(self) -> QuerySet:
            return super().get_queryset().filter(status= "published")
        
    options = (("draft", "Draft"), ("published", "Published"))
    link = models.TextField()
    title = models.CharField(max_length=250)
    linkDescription = models.CharField(max_length=120)
    shortDescription = models.CharField(max_length=250)
    published = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to=filePathImage)
    videoLink = models.CharField(max_length=250, default= "")
    status = models.CharField(max_length= 10, choices=options, default="published")
    
    objects = models.Manager()
    carouselObjects = CarouselObjects()
    
    class Meta:
        ordering = ("-published",)
    
class LanguageExperience(models.Model):
    class LanguageItems(models.Manager):
        def get_queryset(self) -> QuerySet:
            return super().get_queryset().filter(status= "published")
        
    options = (("draft", "Draft"), ("published", "Published"))
    name = models.CharField(max_length=50)
    yearsOfExperience = models.CharField(max_length=50)
    shortDescription = models.TextField(max_length=250)
    published = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to=filePathImage)
    amountOfExperience = models.IntegerField()
    status = models.CharField(max_length= 10, choices=options, default="published")
    
    objects = models.Manager()
    languageObjects = LanguageItems()
    
    class Meta:
        ordering = ("-published",)
    
class SoftwareExperience(models.Model):
    class SoftwareItems(models.Manager):
        def get_queryset(self) -> QuerySet:
            return super().get_queryset().filter(status= "published")
        
    options = (("draft", "Draft"), ("published", "Published"))
    name = models.CharField(max_length=50)
    yearsOfExperience = models.CharField(max_length=50)
    shortDescription = models.TextField(max_length=250)
    published = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to=filePathImage)
    amountOfExperience = models.IntegerField()
    status = models.CharField(max_length= 10, choices=options, default="published")
    
    objects = models.Manager()
    softwareObjects = SoftwareItems()
    
    class Meta:
        ordering = ("-published",)
    
class QualificationExperience(models.Model):
    class QualificationItems(models.Manager):
        def get_queryset(self) -> QuerySet:
            return super().get_queryset().filter(status= "published")
        
    options = (("draft", "Draft"), ("published", "Published"))
    qualificationName = models.CharField(max_length=50)
    startExperience = models.DateField()
    endExperience = models.DateField()
    linkDescription = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    qualificationLink = models.FileField(upload_to=filePathFile)
    image = models.ImageField(upload_to=filePathImage)
    shortDescription = models.TextField(max_length=250)
    status = models.CharField(max_length= 10, choices=options, default="published")
    published = models.DateTimeField(default=timezone.now)
    
    objects = models.Manager()
    qualificationObjects = QualificationItems()
    
    class Meta:
        ordering = ("-published",)
    
class WorkExperience(models.Model):
    class WorkExperiencesObject(models.Manager):
        def get_queryset(self) -> QuerySet:
            return super().get_queryset().filter(status= "published")
        
    options = (("draft", "Draft"), ("published", "Published"))
    companyName = models.CharField(max_length=50)
    startExperience = models.DateField()
    endExperience = models.DateField()
    linkDescription = models.CharField(max_length=50)
    link = models.CharField(max_length=150)
    image1 = models.ImageField(upload_to=filePathImage)
    image2 = models.ImageField(upload_to=filePathImage)
    image3 = models.ImageField(upload_to=filePathImage)
    shortDescription = models.TextField()
    longDescription1 = models.TextField()
    longDescription2 = models.TextField()
    status = models.CharField(max_length= 10, choices=options, default="published")
    published = models.DateTimeField(default=timezone.now)
    objects = models.Manager()
    workExperienceObjects = WorkExperiencesObject()
    
    class Meta:
        ordering = ("-published",)