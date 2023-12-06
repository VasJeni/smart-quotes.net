from django.views.generic import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


class DonorPageView(TemplateView):
    template_name = "donor.html"
