# serializers.py
from rest_framework import serializers
from .models import File


class FileSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.ReadOnlyField(source='uploaded_by.username')
    uploaded_at = serializers.ReadOnlyField()
    file_size = serializers.SerializerMethodField()
    
    class Meta:
        model = File
        fields = ['id', 'course', 'name', 'description', 'file', 'uploaded_by', 'uploaded_at', 'file_size']
        read_only_fields = ['uploaded_by', 'uploaded_at']
    
    def get_file_size(self, obj):
        return obj.get_file_size()
