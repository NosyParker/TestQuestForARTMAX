from django.db import models
from django.utils import timezone

class Note(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    text = models.TextField(max_length=200, verbose_name = "Текст заметки")
    published_date = models.DateTimeField(verbose_name = "Время публикации")


    def publish(self):
        self.published_date = timezone.now()

    
    def __str__(self):
        return self.title