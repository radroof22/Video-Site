"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include,patterns
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "videos"

urlpatterns = [
	url(r'^videos/(?P<pk>[0-9]+)', views.MediaView.as_view(), name = "view_video"),
	url(r'^$', views.IndexView.as_view(), name = "index"),
	url(r'^videos/', views.IndexView.as_view()),

    url(r'^api/video/$',views.VideoList.as_view()),
    url(r'^api/video/(?P<pk>[0-9]+)/$',views.VideoDetail.as_view()),

    url(r'^api/article/$',views.ArticleList.as_view()),
    url(r'^api/article/(?P<pk>[0-9]+)/$',views.ArticleDetail.as_view()),

    url(r'^register/user/$',views.UserRegister.as_view()),
    url(r'^register/video/$',views.VideoRegister.as_view()),
    url(r'^register/article/$',views.ArticleRegister.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
