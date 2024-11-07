from django.db import models
from profiles.models import UserProfile
from products.models import Product


class Wishlist(models.Model):
    """ A model to add favourite products into a wishlist """
    user_profile = models.OneToOneField(
                                    UserProfile,
                                    on_delete=models.CASCADE,
                                    related_name="customer_wishlist",
                                    default=None
                                    )
    product = models.ManyToManyField(
                                Product, default=None
                                )

    def __str__(self):
        """Return the string representation of the model."""
        return str(self.user_profile) + '\'s wishlist'
    # def add_to_wishlist(self, product):
    #     """Add a product to the wishlist."""
    #     # check that product is not already in the wishlist
    #     if product not in self.products.all():
    #         self.products.add(product)
    #         return True
    #     return False
    # def remove_from_wishlist(self, product):
    #     """Remove a product from the wishlist."""
    #     # check that product is in the wishlist
    #     if product in self.products.all():
    #         self.products.remove(product)
    #         return True
    #     return False
    # def remove_all_from_wishlist(self):
    #     """Remove all products from the wishlist."""
    #     self.products.clear()
    #     return True
    # def get_products(self):
    #     """Return the products in the wishlist."""
    #     return self.products.all()
