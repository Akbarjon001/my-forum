from django.db import models
from account.models import CustomUser
from django.utils import timezone

# Create your models here.


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    body = models.TextField(null=True)

    def __str__(self):
        return self.title


def upload_to(instance, filename):
    return 'photos/{0}/{1}'.format(instance.user.username, filename)


class Topics(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    body = models.TextField(null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=upload_to, default=None)
    category = models.CharField(max_length=50, default='others')

    def __str__(self):
        return self.title


class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    text = models.TextField()
    in_topic = models.ForeignKey(Topics, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.in_topic