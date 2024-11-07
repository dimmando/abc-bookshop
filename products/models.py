from django.db import models
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator


class Category(models.Model):
    """Category Models"""
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    LANGUAGES = 'languages'
    MEDICINE = 'medicine'
    HISTORY = 'history'

    CATEGORY_CHOICES = [
        (LANGUAGES, 'languages'),
        (MEDICINE, 'medicine'),
        (HISTORY, 'history'),
    ]

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """ Model for children's books """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
        )
    ean = models.CharField(max_length=13, null=True, blank=True, unique=True)
    ISBN = models.CharField(max_length=13, null=True, blank=True, unique=True)
    title = models.CharField(max_length=254, null=False, blank=False)
    author = models.CharField(max_length=254, null=False, blank=False)
    size = models.CharField(max_length=254, null=True, blank=True)
    number_of_pages = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(
        max_length=1024, default='', null=True, blank=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, validators=[
            MinValueValidator(0.0, message=None)])
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True, validators=[
            MinValueValidator(0.0, message=None)])
    new_arrival = models.BooleanField(blank=True)
    discount = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True
        )
    is_sale = models.BooleanField()
    sale_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True, validators=[
            MinValueValidator(0.0, message=None)])
    by_age = models.CharField(
        max_length=40,
        null=False,
        blank=False,
        choices=[
            ("schoolchildren", "schoolchildren"),
            ("students", "students"),
            ("professionals", "professionals"),
        ],
    )
    image = CloudinaryField('image', null=True, blank=True)

    # To be able to user have final_price as model attribute
    # without having to add a new model field
    @property
    def final_price(self):
        """ If product is on sale, set it's sales price to final price """
        products = Product.objects.all()
        for product in products:
            try:
                if self.is_sale and self.sale_price < self.price:
                    return self.sale_price
                else:
                    return self.price
            except (TypeError, ValueError):
                return None

    def __str__(self):
        return self.title
