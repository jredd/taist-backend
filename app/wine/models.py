from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):

    name = models.CharField(max_length=50)
    date_added = models.DateField(auto_now_add=True)


class Restaurants(models.Model):

    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    date_added = models.DateField(auto_now_add=True)


class Winery(models.Model):

    name = models.CharField(max_length=50, blank=False, unique=True)
    date_added = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=500, blank=False, unique=True)


class WineAlias(models.Model):

    name = models.CharField(max_length=50, blank=False, unique=True)
    site_associated_with = models.URLField()
    date_added = models.DateField(auto_now_add=True)


class Wine(models.Model):

    winery = models.ForeignKey(Winery, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, blank=False,)
    short_name = models.CharField(max_length=15, blank=True)
    vintage = models.DateField(blank=False)
    wine_alias = models.ForeignKey(WineAlias, on_delete=models.CASCADE)
    restaurants = models.ForeignKey(Restaurants, on_delete=models.PROTECT)
    date_added = models.DateField(auto_now_add=True)


class Rating(models.Model):

    wine = models.ForeignKey(Wine, on_delete=models.PROTECT)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    vintage = models.DateField(blank=False)
    date_added = models.DateField(auto_now_add=True)


class Review(models.Model):

    review = models.CharField(max_length=500)
    vintage = models.DateField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    date_added = models.DateField(auto_now_add=True)


