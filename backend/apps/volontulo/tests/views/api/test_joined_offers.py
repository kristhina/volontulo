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

    def test_user_joined_no_offers(self):

        user = UserFactory()
        self.client.login(username=user.username, password=user.password)

        res = self.client.get(ENDPOINT_URL, {'username': user.username, 'password': user.password}, format = 'json')
        self.assertEqual(res.data, [])

    def test_user_joined_one_offer(self):
        # import pdb;
        # pdb.set_trace()
        user = UserFactory()
        self.client.login(username=user.username, password=user.password)
        offer = OfferFactory(
            volunteers=[user]
        )
        res = self.client.get(ENDPOINT_URL, {'username': user.username, 'password': user.password}, format = 'json')
        self.assertEqual(len(res.data), 1)

    def test_user_joined_some_offers(self):
        user = UserFactory()
        self.client.login(username=user.username, password=user.password)

        offer1 = OfferFactory(
            volunteers=[user]
        )
        offer2 = OfferFactory(
            volunteers=[user]
        )
        res = self.client.get(ENDPOINT_URL, {'username': user.username, 'password': user.password}, format = 'json')
        self.assertEqual(len(res.data), 2)
