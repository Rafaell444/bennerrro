from django.contrib import admin
from .models import about, slider, product, category, advantage

# Register your models here.
admin.site.register(slider)
admin.site.register(product)
admin.site.register(about)
admin.site.register(category)
admin.site.register(advantage)
