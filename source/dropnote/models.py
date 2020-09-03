import uuid

from django.db import models
from django.urls import reverse


class TokenField(models.CharField):
    def __init__(self, verbose_name=None, **kwargs):
        kwargs['max_length'] = 6
        kwargs['default'] = self.make_new
        super().__init__(verbose_name, **kwargs)

    @staticmethod
    def make_new():
        return uuid.uuid4().hex[:6]


class SnippetItem(models.Model):
    # рандомный набор символов, чтобы нельзя было проитерироваться по всем заметкам
    id = TokenField(primary_key=True, editable=False)
    # текст в котором хранится сниппет
    text = models.TextField()
    # даты
    date_created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('dropnote:view', args=(self.id,))
