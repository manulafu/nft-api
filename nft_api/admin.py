from django.contrib import admin

from .models import User, Collection, Nft

admin.site.register(User)
admin.site.register(Collection)
admin.site.register(Nft)
