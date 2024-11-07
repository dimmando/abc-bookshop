from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from profiles.models import UserProfile
from products.models import Product
from .models import Wishlist
from django.contrib.auth.decorators import login_required


@login_required
def wishlist(request):
    """ A view to go to user's wishlist entries """

    user_profile = UserProfile.objects.get(user=request.user)
    customer_wishlist = Wishlist.objects.filter(user_profile=user_profile)

    context = {
        'customer_wishlist': customer_wishlist,
        'on_page': True,
    }

    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):
    """ Add the chosen product into the wishlist """

    product = get_object_or_404(Product, pk=product_id)
    user_profile = UserProfile.objects.get(user=request.user)

    wishlist, created = Wishlist.objects.get_or_create(user_profile=user_profile)
    if product in wishlist.product.all():
        messages.warning(request, f'You already have {product.title} in your wishlist.')
    else:
        wishlist.product.add(product)
        messages.success(request, f'You have successfully added {product.title} to your wishlist.')

    return redirect(reverse('wishlist'))
    

@login_required
def remove_from_wishlist(request, product_id):
    
    """ Remove the chosen product from the wishlist """

    product = get_object_or_404(Product, pk=product_id)
    user_profile = UserProfile.objects.get(user=request.user)

    try:
        wishlist = Wishlist.objects.get(user_profile=user_profile)
        if product in wishlist.product.all():
            wishlist.product.remove(product)
            messages.success(request, f'{product.title} was successfully removed from your wishlist.')
        else:
            messages.warning(request, f'{product.title} is not in your wishlist.')
    except Wishlist.DoesNotExist:
        messages.error(request, 'You do not have a wishlist yet.')

    return redirect(reverse('wishlist'))
