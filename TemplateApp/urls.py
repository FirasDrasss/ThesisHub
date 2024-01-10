from django.urls import path
from . import views

app_name = "templateapp"
urlpatterns = [
    path("", views.homepage,name="homepage" ),
]
