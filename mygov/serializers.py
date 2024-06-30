from rest_framework import serializers
from .models import Parents, Children, WorkHistory, Educations


class ParentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parents
        fields = ['id', 'f_number', 'm_number', 'address']


class ChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Children
        fields = ['id', 'ch_number', 'first_name', 'last_name', 'family_id', 'birth_date', 'foto']


class WorkHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkHistory
        fields = '__all__'


class EducationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educations
        fields = '__all__'
