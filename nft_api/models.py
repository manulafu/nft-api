import uuid

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
        
PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

class User(models.Model):

    user_wallet = models.CharField(max_length=255)

    def __str__(self):
        return self.user_wallet
    


class Collection(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    descritption = models.TextField()
    creator = models.ForeignKey(User, related_name="collections", on_delete=models.CASCADE)
    creator_network = models.CharField(max_length=255)

    def __str__(self):
        return f'UUID({self.uuid})-{self.name}'

class Nft(models.Model):

    asset_id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    picture = models.URLField()
    external_link = models.URLField()
    description = models.TextField()
    collection = models.ForeignKey(Collection, related_name='nfts', on_delete=models.CASCADE)
    supply = models.PositiveBigIntegerField()
    royalties = models.DecimalField(max_digits=5, decimal_places=2, default=0, validators=PERCENTAGE_VALIDATOR)
    creation_date = models.DateTimeField(auto_now_add=True)
    buyer = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} from {self.collection.name}'

    class Meta:
        ordering = ('-creation_date', )