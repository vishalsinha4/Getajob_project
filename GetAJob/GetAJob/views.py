from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def applyPage(request):
    return render(request,'ApplyPage/applyPage.html')