# -*- coding: utf-8 -*-

"""
.. module:: test_joined_offers
"""

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase

from apps.volontulo.factories import UserFactory, OrganizationFactory

from backend.apps.volontulo.factories import OfferFactory

ENDPOINT_URL = reverse('joined_offers')


class TestJoinedOffers(APITestCase, TestCase):

    def test_user_joined_no_offers(self):
        user = UserFactory()
        res = self.client.get(ENDPOINT_URL)
        self.assertEqual(res, [])

    def test_user_joined_one_offer(self):
        user = UserFactory()
        offer = OfferFactory(
            volunteers=[user]
        )
        res = self.client.get(ENDPOINT_URL)
        self.assertEqual(len(res), 1)

    def test_user_joined_some_offers(self):
        user = UserFactory()
        offer1 = OfferFactory(
            volunteers=[user]
        )
        offer2 = OfferFactory(
            volunteers=[user]
        )
        res = self.client.get(ENDPOINT_URL)
        self.assertEqual(len(res), 2)
