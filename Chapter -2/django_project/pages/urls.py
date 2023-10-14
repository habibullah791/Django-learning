from django.urls import path
from .views import homePageView

# Define URL patterns for your Django app.
urlpatterns = [
    path("", homePageView, name="home"),
]

