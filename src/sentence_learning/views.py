from django.shortcuts import render

from .models import Sentence

# Create your views here.


def daily_sentence_list(request):
    sentence = Sentence.objects.all()
    context = {
        'sentence_list': sentence
    }
    return render(request, 'sentence_list.html', context)


def write_sentence(request):
    sentence = Sentence.objects.all()
    context = {
        'sentence_list': sentence
    }
    return render(request, 'paint.html', context)
