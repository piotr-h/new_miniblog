from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  title = models.CharField('Tytuł', max_length=300)
  text = models.TextField('Treść')
  created_date = models.DateTimeField('Data utworzenia', default=timezone.now)
  edited_date = models.DateTimeField('Data edycji', default=timezone.now)

  def publish(self):
    self.save()

  def get_absolute_url(self):
    return reverse('post_detail', args=[str(self.id)])

  def __str__(self):
    return self.title



