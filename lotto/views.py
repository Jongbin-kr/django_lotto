from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import GuessNumbers
from .forms import PostForm

import random

import numpy as np

# Create your views here.
def index(request):
    
    lottos = GuessNumbers.objects.all()
    
    return render(request, 'lotto/default.html', {'lottos': lottos})


def hello(request):
    return HttpResponse("<h1 style='color:red'>Hello, world!</h1>")


def post(request):

    if request.method == 'POST':
        print(request.POST)
        form = PostForm(request.POST)
        
        if form.is_valid(): ## 채워진 양식에 대해 validation check
            lotto = form.save(commit=False)
            lotto.generate()
            
            return redirect('index')
        
        print(type(form))
        print(form)
        
    else:
        form = PostForm()
        return render(request, 'lotto/form.html', {'form': form})
    

def detail(request, lottokey):
    
    lotto = GuessNumbers.objects.get(id=lottokey)
    
    return render(request, 'lotto/detail.html', {'lotto':lotto})