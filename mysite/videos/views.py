from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .models import Video
from django.views import generic
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Video,Article
from .serializers import VideoSerializer,ArticleSerializer
from .forms import UserForm,ArticleForm,VideoForm
from django.views.generic import View


# Create your views here.



# Create your views here.
class IndexView(generic.ListView):
	template_name = "video/index_orig.html"
	context_object_name = "all_videos"

	def get_queryset(self):
		return Video.objects.all()

class MediaView(generic.DetailView):
	model = Video
	template_name = "video/detail.html"

class VideoList(generics.ListCreateAPIView):
	queryset = Video.objects.all()
	serializer_class = VideoSerializer

class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Video.objects.all()
	serializer_class = VideoSerializer

class ArticleList(generics.ListCreateAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

class UserRegister(View):
	form_class = UserForm
	template_name = "video/register.html"

	#display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request,self.template_name,{"form":form})

	#proccess form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)

			#cleaned (normailize) data
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]

			#set user password
			user.set_password(password)
			#save contents username
			user.save()

			#retur User objects if cred is correct
			user = authenticate(username=username,password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect("video:index")

		return render(request,self.template_name,{"form":form})

class ArticleRegister(View):
	form_class = ArticleForm
	template_name = "video/register.html"

	#display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request,self.template_name,{"form":form})

	#proccess form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)

			#save contents username
			user.save()

			if user is not None:

					return redirect("video:index")

		return render(request,self.template_name,{"form":form})

class VideoRegister(View):
	form_class = VideoForm
	template_name = "video/register.html"

	#display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request,self.template_name,{"form":form})

	#proccess form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)

			#save contents username
			user.save()

			if user is not None:

					return redirect("video:index")

		return render(request,self.template_name,{"form":form})
