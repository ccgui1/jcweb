# Register your models here.
from django.contrib import admin
from .models import ConpanyMoney
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.
admin.AdminSite.site_header = '建策科技管理系统'
admin.AdminSite.site_title = '建策科技管理系统'


class CMoneyAdmin(ImportExportActionModelAdmin):
    list_display = (
        'device_name',
        'buy_date',
        'buy_name',
        'device_type',
        'device_number',
        'device_price',
    )
    search_fields = [
        'device_name',
        'buy_date',
        'buy_name',
        'device_type',
        'device_number',
        'device_price',
    ]
    list_per_page=20

admin.site.register(ConpanyMoney, CMoneyAdmin)
