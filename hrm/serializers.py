from rest_framework import serializers
from hrm.models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('name', 'employee_id')
        # fields = '__all__'
