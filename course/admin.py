from django.contrib import admin
from .models import Course, File


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'file_count')
    search_fields = ('name',)
    ordering = ('name',)
    
    def file_count(self, obj):
        return obj.files.count()
    file_count.short_description = 'Number of Files'


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'uploaded_by', 'uploaded_at', 'file_size')
    list_filter = ('course', 'uploaded_at', 'uploaded_by')
    search_fields = ('name', 'description', 'course__name')
    readonly_fields = ('uploaded_at', 'uploaded_by')
    ordering = ('-uploaded_at',)
    date_hierarchy = 'uploaded_at'
    
    def file_size(self, obj):
        if obj.file:
            size = obj.file.size
            if size < 1024:
                return f'{size} B'
            elif size < 1024 * 1024:
                return f'{size / 1024:.2f} KB'
            else:
                return f'{size / (1024 * 1024):.2f} MB'
        return 'N/A'
    file_size.short_description = 'File Size'
    
    def save_model(self, request, obj, form, change):
        if not change:  # If creating a new object
            obj.uploaded_by = request.user
        super().save_model(request, obj, form, change)
