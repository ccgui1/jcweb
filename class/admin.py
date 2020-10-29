from django.contrib import admin
from .models import ClassJob
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.
admin.AdminSite.site_header = '建策科技管理系统'
admin.AdminSite.site_title = '建策科技管理系统'


class ClassJobAdmin(ImportExportActionModelAdmin):
    list_display = (
        'class_name',
        'class_type',
        'class_time',
        'class_teacher',
        'class_number',
        'class_link',

    )
    search_fields = [
        'class_name',
        'class_type',
        'class_time',
        'class_teacher',
        'class_number',
        'class_link',
    ]
    list_per_page=20

admin.site.register(ClassJob, ClassJobAdmin)
