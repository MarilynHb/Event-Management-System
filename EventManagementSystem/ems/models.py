from django.db import models

#create a model for user
class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    biography = models.TextField()
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    followers_count = models.IntegerField(default=0)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
