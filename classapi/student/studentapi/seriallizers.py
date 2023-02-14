from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    sid =  serializers.IntegerField()
    name = serializers.CharField(max_length=200)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=200)

    # def create():
    #    return Student.objects.create()

    def create(self, validated_data,many=True):
        return Student.objects.create(**validated_data)