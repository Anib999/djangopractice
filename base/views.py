from django.shortcuts import render

# Create your views here.

def viewAllRoutes(request):
    context = {}
    return render(request, 'base/index.html', context)