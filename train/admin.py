# Register your models here.
from django.contrib import admin
from .models import TrainJob
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.
admin.AdminSite.site_header = '建策科技管理系统'
admin.AdminSite.site_title = '建策科技管理系统'


class TrainJobAdmin(ImportExportActionModelAdmin):
    list_display = (
        'train_school',
        'train_class',
        'train_lesson',
        'start_time',
        'end_time',
        'train_teacher',
        'train_leader',
        'tel_number',
    )
    search_fields = [
        'train_school',
        'train_class',
        'train_lesson',
        'start_time',
        'end_time',
        'train_teacher',
        'train_leader',
        'tel_number',
    ]
    list_per_page=20

admin.site.register(TrainJob, TrainJobAdmin)
