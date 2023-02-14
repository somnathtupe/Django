from rest_framework import serializers
from .models import Author

class AuthorSerializer(serializers.Serializer):
     first_name = serializers.CharField(max_length=200)
     last_name = serializers.CharField(max_length=200)
     date_of_joining = serializers.DateField()

    

     def create(self, validated_data,many=True):
        return Author.objects.create(**validated_data)

    #  def get_or_create(cls, **kwargs):
    #      try:
    #         instance, created = cls.get(**kwargs), False
    #      except cls.DoesNotExist:
    #         instance, created = cls.create(**kwargs), True
    #      return instance, created
    #  def validated_data(self,name):
    #      if Author.first_name==name:
    #         raise serializers.ValidationError("name alreday present")
    #      return name

