from django.contrib import admin
from .models import PJManager
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.
admin.AdminSite.site_header = '建策科技管理系统'
admin.AdminSite.site_title = '建策科技管理系统'


class PManagerAdmin(ImportExportActionModelAdmin):
    list_display = (
        'projectManager_name',
        'projectManager_time',
        'projectMoney_name',
        'Project_leader',
        'Project_rate',
    )
    search_fields = [
        'projectManager_name',
        'projectManager_time',
        'projectMoney_name',
        'Project_leader',
        'Project_rate',
    ]
    list_per_page=20

admin.site.register(PJManager, PManagerAdmin)
