from django.urls import path
from .views import PostList, PostDetail,CarouselList,CarouselDetail,SoftwareList,SoftwareDetail,QualificationDetail,QualificationList,LanguageDetail,LanguageList,WorkExperienceList,WorkExperienceDetail
app_name = 'blog_api'

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('', PostList.as_view(), name='listcreate'),
    path('carousel/<int:pk>/', CarouselDetail.as_view(), name='detailcreate'),
    path('carousel/', CarouselList.as_view(), name='listcreate'),
    path('software/<int:pk>/', SoftwareDetail.as_view(), name='detailcreate'),
    path('software/', SoftwareList.as_view(), name='listcreate'),
    path('qualification/<int:pk>/', QualificationDetail.as_view(), name='detailcreate'),
    path('qualification/', QualificationList.as_view(), name='listcreate'),
    path('language/<int:pk>/', LanguageDetail.as_view(), name='detailcreate'),
    path('language/', LanguageList.as_view(), name='listcreate'),
    path('workExperience/<int:pk>/', WorkExperienceDetail.as_view(), name='detailcreate'),
    path('workExperience/', WorkExperienceList.as_view(), name='listcreate'),
]
