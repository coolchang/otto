from django.db import models

# Create your models here.


class Sentence(models.Model):

    sentence_id = models.CharField(max_length=20)  # sentence id
    sentence = models.TextField()  # sentence content
    meaning = models.TextField(default='문장 뜻')  # sentence meaning

    def __str__(self):
        return self.sentence
