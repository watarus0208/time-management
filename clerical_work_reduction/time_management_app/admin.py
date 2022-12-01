from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'password', 'last_login')
    
    
class ContractCompaniesAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'zip_code', 'president', 'phone_number', 'user')


class SalesPeopleAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'mobile_phone_number', 'user', 'company')


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'start_date', 'last_date', 'upper_work_hours', 'lower_work_hours', 'assigned_job', 'summary', 'user', 'company')


class WorkPatternAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'close_time', 'start_break_time', 'close_break_time', 'start_overtime_break', 'close_overtime_break', 'round_down_unit')


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('date', 'start_time', 'close_time', 'user', 'project', 'work_pattern')


admin.site.register(models.User, UserAdmin)
admin.site.register(models.ContractCompanies, ContractCompaniesAdmin)
admin.site.register(models.SalesPeople, SalesPeopleAdmin)
admin.site.register(models.Projects, ProjectsAdmin)
admin.site.register(models.WorkPattern, WorkPatternAdmin)
admin.site.register(models.Attendance, AttendanceAdmin)

