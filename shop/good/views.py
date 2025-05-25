from django.shortcuts import render
from . import models

def main(request):
    context = {
        'good': models.Good.objects.all()
    }
    return render(
        request,
        'good/index.html',
        context      
    )
