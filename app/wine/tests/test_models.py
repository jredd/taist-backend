import datetime

from django.test import TestCase

from .. import models


class WineTestCase(TestCase):
    # fixtures = ['wine_views_test_data.json']

    def setUp(self):
        super(WineTestCase, self).setUp()
        # self.wine_1 = models.Wine.objects.get(id=1)
        # self.wine_2 = models.Wine.objects.get(id=2)

    def test_defaults(self):
        company = models.Company(name='some company name')
        company.save()
        restaurant = models.Restaurants(name='rest1', location='some location', company=company)
        restaurant.save()
        winery = models.Winery(name='some winery name', location='some location')
        winery.save()
        wine_alias = models.WineAlias(name='some alias name', site_associated_with='https//:google.com')
        wine_alias.save()

        now = datetime.datetime.now()
        wine = models.Wine.objects.create(
            name="Some Wine",
            vintage=now,
            winery=winery,
            wine_alias=wine_alias,
            restaurants=restaurant
        )
        print('turtles:', wine.name, wine.date_added)
        self.assertEqual(wine.date_added, now.date())
