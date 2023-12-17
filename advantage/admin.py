from django.contrib import admin
from .models import Adventage

# Register your models here.


class AdventageAdmin(admin.ModelAdmin):
    list_display = (
        "title_en",
        "title_uk",
        "img",
    )


admin.site.register(Adventage, AdventageAdmin)
