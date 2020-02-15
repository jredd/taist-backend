from django.db import models


# Create your models here.
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
    vintage = models.DateField(blank=False)
    wine_alias = models.ForeignKey(WineAlias, on_delete=models.CASCADE)


class Review(models.Model):

    review = models.CharField(max_length=500)
    vintage = models.DateField(blank=True)


