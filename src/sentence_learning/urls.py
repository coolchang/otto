from django.urls import path
from .models import Sentence

from .views import daily_sentence_list, write_sentence

urlpatterns = [
    path('', daily_sentence_list),
    path('write/', write_sentence),
]
