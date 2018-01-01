from rest_framework import serializers
from .models import Video, Article

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ("id",'date',"title","description","video","creator")

class ArticleSerializer(serializers.ModelSerializer):
    video = VideoSerializer()
    class Meta:
        model = Article
        fields = ('id','video',"context")
