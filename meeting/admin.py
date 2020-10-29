
# Register your models here.
from django.contrib import admin
from .models import JCmeeting
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.
admin.AdminSite.site_header = '建策科技管理系统'
admin.AdminSite.site_title = '建策科技管理系统'


class JCmeetingAdmin(ImportExportActionModelAdmin):
    list_display = (
        'meeting_name',
        'start_time',
        'host_name',
        'meeting_number',
        'meeting_link',
    )
    search_fields = [
        'meeting_name',
        'start_time',
        'host_name',
        'meeting_number',
        'meeting_link',
    ]
    list_per_page=20

admin.site.register(JCmeeting, JCmeetingAdmin)
