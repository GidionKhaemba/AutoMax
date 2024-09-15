from django.contrib import admin

from .models import Listing, LikedListing

class ListingAdmin(admin.ModelAdmin):
    readonly_fields=('id',)
    
    pass
admin.site.register(Listing, ListingAdmin)
class LikedListingAdmin(admin.ModelAdmin):
    readonly_fields=('id',)
admin.site.register(LikedListing, LikedListingAdmin )    
