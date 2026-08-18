from rest_framework import serializers
from jobs.models import Job
import bcrypt
from accounts.models import User

class JobSerializer(serializers.ModelSerializer):
    username=serializers.CharField(source="user.username",read_only=True)
    class Meta:
        model=Job
        fields="__all__"
