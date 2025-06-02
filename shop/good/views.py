from django.shortcuts import render
from . import models

def main(request, uprice):
    context = {
        # 'good': models.Good.objects.filter(price = uprice),
        'good': models.Good.objects.all(),
        'uprice': uprice
    }
    return render(
        request,
        'good/index.html',
        context      
    )

from . import forms

def new_good(request):
    context = {
        'new_good_post': forms.GoodPostForm()
    }

    form = forms.GoodPostForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()

    return render(
        request,
        'good/new_good.html',
        context
    )
