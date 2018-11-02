from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='akinator-home'),
	path('question/', views.question, name='akinator-question'),
	path('prototipo_akinator/', views.prototipo_akinator, name='prototipo_akinator'),
	path('answer/', views.answer, name='akinator-answer'),
	
]