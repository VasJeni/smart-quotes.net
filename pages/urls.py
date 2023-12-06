from django.urls import path

from .views import HomePageView, DonorPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("donor/", DonorPageView.as_view(), name="donor"),
]
