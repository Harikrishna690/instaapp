from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.conf import settings

#this is abstract user using the default admin user
class User(AbstractUser):
    phone_number = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(max_length=200, null=True, blank=True)
    Image = models.ImageField(upload_to='images/', null=True, blank=True)
    private = models.BooleanField(default=False)


class Images(models.Model): #this is for the images
    Image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.CharField(max_length=120, null=True, blank=True)
    uploaded_date = models.DateTimeField(auto_now=True)
    person_uploaded = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class Comments(models.Model):#this is for the comments
    ImagesId = models.ForeignKey(Images, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200, null=True, blank=True)
    Parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)


class Liked(models.Model):#this is for the likes
    ImageId = models.ForeignKey(Images, on_delete=models.CASCADE, null=True, blank=True)
    personId = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    commentId = models.ForeignKey(Comments, on_delete=models.CASCADE, null=True, blank=True)

