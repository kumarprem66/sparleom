from rest_framework import serializers
from .models import Assignment


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'