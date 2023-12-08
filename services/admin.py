from django.contrib import admin

# Register your models here.

from .models import Services


class ServicesAdmin(admin.ModelAdmin):
    list_display = (
        "title_en",
        "title_uk",
    )


admin.site.register(Services, ServicesAdmin)
