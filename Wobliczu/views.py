from django.shortcuts import render

# Create your views here.

def renderHome(request):
    return render(request, 'main.html')

def renderKontakt(request):
    return render(request, 'kontakt.html')

def renderInfo(request):
    return render(request, 'o_nas.html')