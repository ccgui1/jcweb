from django.contrib import admin
from .models import MarketFollow
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.
admin.AdminSite.site_header = '建策科技管理系统'
admin.AdminSite.site_title = '建策科技管理系统'


class MarketFollowAdmin(ImportExportActionModelAdmin):
    list_display = (
        'start_time',
        'thing_name',
        'leader_name',
        'quarter_first',
        'quarter_second',
        'quarter_third',
        'quarter_forth',
    )
    search_fields = [
        'start_time',
        'thing_name',
        'leader_name',
        'quarter_first',
        'quarter_second',
        'quarter_third',
        'quarter_forth',
    ]
    list_per_page=20

admin.site.register(MarketFollow,MarketFollowAdmin)