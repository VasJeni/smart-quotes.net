from django.views.generic import TemplateView, ListView
from services.models import Services
from feedback.models import Feedback
from advantage.models import Adventage
from django.utils.translation import get_language_from_request

# Create your views here.


class HomePageView(ListView):
    template_name = "home.html"

    def get_queryset(self):
        services = Services.objects.all()
        return services

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        advantages = Adventage.objects.all()
        services = Services.objects.all()
        feedback = Feedback.objects.all()
        context["advantages"] = advantages
        context["services"] = services
        context["feedbacks"] = feedback
        context["language_code"] = get_language_from_request(self.request)
        return context


class DonorPageView(TemplateView):
    template_name = "donor.html"
