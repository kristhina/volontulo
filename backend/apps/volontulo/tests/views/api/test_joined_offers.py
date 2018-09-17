# -*- coding: utf-8 -*-

"""
.. module:: test_joined_offers
"""

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase

from apps.volontulo.factories import UserFactory, OrganizationFactory
from apps.volontulo.factories import OfferFactory

ENDPOINT_URL = reverse('joined_offers')


class TestJoinedOffers(APITestCase, TestCase):
    """ Tests for joined-offers api"""

    def test_user_joined_no_offers(self):
        """ Tests if user did not join any offer"""

        user = UserFactory()
        self.client.force_login(user=user)

        res = self.client.get(ENDPOINT_URL, {'username': user.username, 'password': user.password}, format='json')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, [])

    def test_user_joined_one_offer(self):
        """Tests if user joined one offer"""

        user = UserFactory()
        self.client.force_login(user=user)

        offer = OfferFactory(image=None)
        offer.volunteers.add(user)

        res = self.client.get(ENDPOINT_URL, {'username': user.username, 'password': user.password}, format='json')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data), 1)

    def test_user_joined_some_offers(self):
        """Tests if user joined more than one offer"""

        user = UserFactory()
        self.client.force_login(user=user)

        offer1 = OfferFactory(image=None)
        offer1.volunteers.add(user)
        offer2 = OfferFactory(image=None)
        offer2.volunteers.add(user)
        offer3 = OfferFactory(image=None)

        res = self.client.get(ENDPOINT_URL, {'username': user.username, 'password': user.password}, format='json')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data), 2)
