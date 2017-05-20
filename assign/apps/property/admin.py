from django.contrib import admin
from apps.property.models import Location, Prop


class LocationAdmin(admin.ModelAdmin):
    pass

class PropAdmin(admin.ModelAdmin):
    pass
# Register your models here.
admin.site.register(Location, LocationAdmin)
admin.site.register(Prop, PropAdmin)
