from django.contrib import admin
from .models import ExtensionJob
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.
admin.AdminSite.site_header = '建策科技管理系统'
admin.AdminSite.site_title = '建策科技管理系统'


class ExtensionJobAdmin(ImportExportActionModelAdmin):
    list_display = (
        'extension_name',
        'extension_leader',
        'extension_target',
        'start_time',
        'end_time',
        'extension_effect',
    )
    search_fields = [
        'extension_name',
        'extension_leader',
        'extension_target',
        'start_time',
        'end_time',
        'extension_effect',
    ]
    list_per_page=20

admin.site.register(ExtensionJob, ExtensionJobAdmin)
