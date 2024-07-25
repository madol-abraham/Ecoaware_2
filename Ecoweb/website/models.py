from django.db import models

# Create your models here.
class Donation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.IntegerField()
    message = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', default='default_image_path/default_image.jpg')
    date_posted = models.DateTimeField(auto_now_add=True)

class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)





