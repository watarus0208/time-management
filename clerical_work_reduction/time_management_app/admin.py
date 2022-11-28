from django.contrib import admin
from . import models

admin.site.register(models.User)
admin.site.register(models.ContractCompanies)
admin.site.register(models.SalesPeople)
admin.site.register(models.Projects)
admin.site.register(models.Attendance)
admin.site.register(models.WorkPattern)