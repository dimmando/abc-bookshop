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
