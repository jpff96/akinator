from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='akinator-home'),
	path('question/', views.question, name='akinator-question'),
	path('answer/', views.answer, name='akinator-answer'),
	
]