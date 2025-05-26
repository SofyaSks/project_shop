from django.shortcuts import render
from . import models

def main(request):
    context = {
        'good': models.Good.objects.filter(price__lt = 100)
    }
    return render(
        request,
        'good/index.html',
        context      
    )
