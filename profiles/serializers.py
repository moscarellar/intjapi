# profiles/serializers.py

from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'  # You can specify the fields you want to include instead of '__all__' if needed

