from rest_framework import serializers
from blog.models import Post, Carousel, LanguageExperience,SoftwareExperience, QualificationExperience, WorkExperience

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "author", "excerpt","content","status")
        
class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = ("id", "link", "title","linkDescription","shortDescription", "image","videoLink","status")
        
class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualificationExperience
        fields = ("qualificationName", "startExperience", "endExperience","linkDescription","link", "qualificationLink","image", "shortDescription","status")
        
class SoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftwareExperience
        fields = ("name", "yearsOfExperience", "shortDescription","image","amountOfExperience","status")
        
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageExperience
        fields = ("name", "yearsOfExperience", "shortDescription","image","amountOfExperience","status")
        
class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ("companyName", "startExperience", "endExperience","linkDescription","link", "image1","image2","image3", "shortDescription", "longDescription1", "longDescription2","status")