from django.urls import path, re_path
from . import views

urlpatterns = [
    path("api/get/assasins", views.get_assasins),
    path("api/get/hits", views.get_hits),
    path("api/track/assasination", views.track_assasination),
    path("api/place/order", views.place_order),
]
