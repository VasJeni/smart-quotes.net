from django.views.generic import TemplateView, ListView
from services.models import Services
from django.utils.translation import get_language_from_request

# Create your views here.


class HomePageView(ListView):
    model = Services
    context_object_name = "service_list"
    template_name = "home.html"

    def get_queryset(self):
        language = get_language_from_request(self.request)

        if language == "uk":
            # Витягуємо дані з першої та другої колонок бази даних
            return Services.objects.only("title_uk", "description_uk")
        else:
            # Витягуємо дані з третьої та четвертої колонок бази даних
            return Services.objects.only("title_en", "description_en")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "lang": get_language_from_request(self.request),
                # "queryset": super().get_queryset(),
            }
        )
        return context


class DonorPageView(TemplateView):
    template_name = "donor.html"
