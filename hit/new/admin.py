from django.contrib import admin
from . import models as M
# Register your models here.
admin.site.register(M.Food_items)
admin.site.register(M.Soft_drinks)
admin.site.register(M.Bill_Items)