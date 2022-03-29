from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.core.management import call_command

from .models import User, Collection, Nft

class TestAPI(APITestCase):

    def setUp(self):
        # We prepopulate the test DB
        call_command('loaddata', 'nft_api/fixtures/tests.json')

    def test_nft_list(self):
        response = self.client.get(reverse('nft-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(
            response.data[0]['creation_date'],
            response.data[-1]['creation_date']
        )
        
    def test_mint_nft(self):
        collection = Collection.objects.first()
        nft = {
            "asset_id": "test",
            "name": "Test name",
            "picture": "https://linkedin.com/",
            "external_link": "https://google.com/",
            "description": "Test description",
            "supply": 1,
            "royalties": 12,
            "buyer": "Test Buyer",
            "collection": collection.uuid
        }
        response = self.client.post(reverse('nft-mint'), nft)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_nft_detail(self):
        nft = Nft.objects.first()
        # Good request
        good_response = self.client.get(reverse('nft-detail', kwargs={'asset_id': nft.asset_id}))
        self.assertEqual(good_response.status_code, status.HTTP_200_OK)
        # Bad request
        bad_response = self.client.get(reverse('nft-detail', kwargs={'asset_id': 'random'}))
        self.assertEqual(bad_response.status_code, status.HTTP_404_NOT_FOUND)

    def test_collection_list(self):
        response = self.client.get(reverse('collection-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


    def test_collection_detail(self):
        collection = Collection.objects.first()

        good_response = self.client.get(reverse('collection-detail', kwargs={'uuid': collection.uuid}))
        self.assertEqual(good_response.status_code, status.HTTP_200_OK)
        bad_response = self.client.get(reverse('collection-detail', kwargs={'uuid': 'bad uuid'}))
        self.assertEqual(bad_response.status_code, status.HTTP_404_NOT_FOUND)