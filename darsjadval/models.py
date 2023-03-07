from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

class Darsjadval(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=200, blank=True)
    #body = models.TextField()
    body = RichTextField()
    photo = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('jadval_detail', args=[str(self.id)])

class Izoh(models.Model):
    darsjadval = models.ForeignKey(Darsjadval, on_delete=models.CASCADE, related_name='izohlar')
    izoh = models.CharField(max_length=150)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.izoh

    def get_absolute_url(self):
        return reverse('jadval_list')

