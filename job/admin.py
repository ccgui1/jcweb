from django.contrib import admin
from .models import StudentJob
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.
admin.AdminSite.site_header = '建策科技管理系统'
admin.AdminSite.site_title = '建策科技管理系统'


class StudentJobAdmin(ImportExportActionModelAdmin):
    list_display = (
        'student_id', 
        'student_name', 
        'school_name', 
        'start_time', 
        'end_time', 
        'company_name', 
        'job_name',
    )
    search_fields = [
        'student_id', 
        'student_name', 
        'school_name', 
        'start_time', 
        'end_time', 
        'company_name', 
        'job_name',
    ]
    list_per_page=20

admin.site.register(StudentJob, StudentJobAdmin)
