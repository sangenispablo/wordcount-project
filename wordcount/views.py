from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html', {'nombre':'Pablo Sangenis'})

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddicc = {}
    for word in wordlist:
        if word in worddicc:
            worddicc[word] += 1
        else:
            worddicc[word] = 1
    
    # Esto seria bueno buscar mejor como funciona, es ordenar un diccionario
    sortedword = sorted(worddicc.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {
        'fulltext':fulltext, 
        'count':len(wordlist), 
        'sortedword':sortedword
        })

def about(request):
    return render(request, 'about.html')