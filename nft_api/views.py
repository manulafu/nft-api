from django.shortcuts import render
from rest_framework import generics

from .serializers import *
from .models import *


class NftMintView(generics.CreateAPIView):
    queryset = Nft.objects.all()
    serializer_class = NftSerializer

class NftView(generics.RetrieveAPIView):
    queryset = Nft.objects.all()
    serializer_class = NftSerializer
    lookup_field = 'asset_id'

class NftList(generics.ListAPIView):
    queryset = Nft.objects.all()
    serializer_class = NftSerializer

class CollectionList(generics.ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

class CollectionView(generics.RetrieveAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    lookup_field = 'uuid'
