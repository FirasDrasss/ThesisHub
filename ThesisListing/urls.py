from django.urls import path
from . import views
from .views import (
    ListingsView,
    ListingCreateView,
    ListingDetailView

)

urlpatterns = [
    path('', ListingsView.as_view(), name='listing_main'),
    path('<int:pk>/',ListingDetailView.as_view(), name='listing_view'),
    path('create/',ListingCreateView.as_view(), name='listing_create_view'),
    path('ajax/load-institutes/', views.load_institutes, name='ajax_load_institutes'),
]
