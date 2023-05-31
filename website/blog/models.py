from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    post_image = models.ImageField(default='default2.jpg', upload_to='postpic.pic/')
    favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)


    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.post_image.path)
    #     size = (400, 400)
    #     if img.height > 400 or img.width > 400:
    #         img.thumbnail(size)
    #         img.save(self.post_image.path)
