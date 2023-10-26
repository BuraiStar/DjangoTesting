from rest_framework import generics
from blog.models import Post, Carousel,WorkExperience,LanguageExperience,SoftwareExperience, QualificationExperience
from .serializers import PostSerializer, CarouselSerializer, QualificationSerializer, SoftwareSerializer,LanguageSerializer, WorkExperienceSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.postObjects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CarouselList(generics.ListCreateAPIView):
    queryset = Carousel.carouselObjects.all()
    serializer_class = CarouselSerializer
    
class QualificationList(generics.ListCreateAPIView):
    queryset = QualificationExperience.qualificationObjects.all()
    serializer_class = QualificationSerializer
    
class SoftwareList(generics.ListCreateAPIView):
    queryset = SoftwareExperience.softwareObjects.all()
    serializer_class = SoftwareSerializer
    
class WorkExperienceList(generics.ListCreateAPIView):
    queryset = WorkExperience.workExperienceObjects.all()
    serializer_class = WorkExperienceSerializer
    
class LanguageList(generics.ListCreateAPIView):
    queryset = LanguageExperience.languageObjects.all()
    serializer_class = LanguageSerializer

class CarouselDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer

class SoftwareDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SoftwareExperience.objects.all()
    serializer_class = SoftwareSerializer

class QualificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QualificationExperience.objects.all()
    serializer_class = QualificationSerializer

class LanguageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LanguageExperience.objects.all()
    serializer_class = LanguageSerializer

class WorkExperienceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer
    

""" Concrete View Classes
#CreateAPIView
Used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
##ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""