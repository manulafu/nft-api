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

class NftList(generics.ListAPIView):
    queryset = Nft.objects.all().order_by('-creation_date')
    serializer_class = NftSerializer
