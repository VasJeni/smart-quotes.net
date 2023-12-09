from django.views.generic import TemplateView, ListView
from services.models import Services
from feedback.models import Feedback
from django.utils.translation import get_language_from_request

# Create your views here.


class HomePageView(ListView):
    # model = Services
    # context_object_name = "service_list"
    template_name = "home.html"

    def get_queryset(self):
        services = Services.objects.all()
        return services

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        services = Services.objects.all()
        feedback = Feedback.objects.all()
        context["services"] = services
        context["feedbacks"] = feedback
        context["lang"] = get_language_from_request(self.request)
        return context


class DonorPageView(TemplateView):
    template_name = "donor.html"
