from django.urls import path

from .views import *


urlpatterns = [
    path('NFT/all/', NftList.as_view(), name='nft-list'),
    path('NFT/<str:asset_id>/', NftView.as_view(), name='nft-detail'),
    path('collection/all/', CollectionList.as_view(), name='collection-list'),
    path('collection/<str:uuid>/', CollectionView.as_view(), name='collection-detail'),
    path('mint/', NftMintView.as_view(), name='nft-mint')
]