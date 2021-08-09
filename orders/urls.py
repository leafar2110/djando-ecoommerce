from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.order, name='order'),
    path('address', views.address, name='address'),
    path('select/address', views.select_address, name='select_address'),
    path('set/address/<int:pk>', views.check_address, name='check_address'),
    path('confirm', views.confirm, name='confirm'),
    path('cancelar', views.cancel, name='cancel'),
    path('complete', views.complete, name='complete'),
    path('completed', views.OrderListView.as_view(), name='completeds')
    
]