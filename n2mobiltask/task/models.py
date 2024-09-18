from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=100)
    suite = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)

class Geo(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()

class Company(models.Model):
    name = models.CharField(max_length=100)

class Users(models.Model):
    name = models.CharField(max_length=50, blank=False)
    username = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=50, blank=False)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    geo = models.OneToOneField(Geo, on_delete=models.CASCADE)
    phone = models.CharField(max_length=17)
    website = models.CharField(max_length=100)
    company = models.OneToOneField(Company, on_delete=models.CASCADE)

class Albums(models.Model):
    userId = models.ForeignKey(Users, related_name='albums', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

class Photos(models.Model):
    albumId = models.ForeignKey(Albums, related_name='photos', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url = models.URLField()
    thumbnail_url = models.URLField()

class Posts(models.Model):
    userId = models.ForeignKey(Users, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()

class Comments(models.Model):
    postId = models.ForeignKey(Posts, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()

class Todos(models.Model):
    userId = models.ForeignKey(Users, related_name='todos', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
