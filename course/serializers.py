# serializers.py
from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['course', 'name', 'description', 'file', 'uploaded_by', 'uploaded_at']
