from rest_framework import serializers

from .models import User, Collection, Nft


class UserSerializer(serializers.ModelSerializer):
   class Meta:
        model = User
        fields = '__all__'

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'
    
class NftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nft
        fields = '__all__'
