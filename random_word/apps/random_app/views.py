from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    ran_string= get_random_string(length=14)
    random={
        'word':ran_string
    }
    if 'contador' not in request.session:
        request.session['contador']=1
    
    return render(request,'index.html', random)

def random_word(request):
    request.session['contador'] += 1
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
