from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'akinator/index.html')

def question(request):
	return render(request,'akinator/question.html')

def answer(request):
	return render(request,'akinator/answer.html')