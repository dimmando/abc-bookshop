from django.contrib import admin
from .models import UserProfile
from wishlist.models import Wishlist

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_wishlist_products')

    def get_wishlist_products(self, obj):
        wishlist = Wishlist.objects.filter(user_profile=obj).first()
        if wishlist:
            return ', '.join([product.title for product in wishlist.product.all()])
        return 'No products'

    get_wishlist_products.short_description = 'Wishlist Products'

admin.site.register(UserProfile, UserProfileAdmin)


# from django.contrib import admin
# from .models import Wishlist


# class WishlistAdmin(admin.ModelAdmin):
#     """Wishlist"""
#     model = Wishlist
#     # fields = ('user_profile', 'product')
#     # list_display = ('user_profile', 'product')


# admin.site.register(Wishlist, WishlistAdmin)
