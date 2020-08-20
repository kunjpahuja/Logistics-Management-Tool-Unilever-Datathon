from django.contrib import admin

# Register your models here.

from .models import Plant, Cost, Operation, Consolidated_Data

admin.site.register(Plant)
admin.site.register(Cost)
admin.site.register(Operation)
admin.site.register(Consolidated_Data)
