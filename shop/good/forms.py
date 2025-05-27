from django import forms
from . import models

class GoodPostForm(forms.ModelForm):
    class Meta():
        model = models.Good

        fields = [
            'g_name',
            'price',
            'g_type'
        ]

        labels = {
            'g_name':'Название товара' ,
            'price' :'Цена' ,
            'g_type' : 'Тип товара'
        }