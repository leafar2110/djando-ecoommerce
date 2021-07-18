from django.shortcuts import render
from .models import ShippingAddress
from django.views.generic import ListView
from users.models import User
# Create your views here.

class ShippingAddressListView(ListView):
    model = ShippingAddress
    template_name = 'shipping_addresses/shipping_addresses.html'

    def get_queryset(self):
        return ShippingAddress.objects.filter(user=self.request.user).order_by('-default')