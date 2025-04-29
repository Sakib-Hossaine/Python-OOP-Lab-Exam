from django.db import models

class Author(models.Model):
   name = models.CharField(max_length=100)
   bio = models.TextField(blank=True)
   email = models.EmailField(unique=True)
   created_at = models.DateTimeField(auto_now_add=True)
   profile_pic = models.ImageField(upload_to='profile/', blank=True, null=True)
   def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Hospital(models.Model):
    hospital_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    number_of_doctors = models.IntegerField()

    def __str__(self):
        return self.hospital_name





