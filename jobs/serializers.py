from .models import Job, Language
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Job Serializer
class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # Model serializes it
        model = Job
        fields = ['id', 'title', 'description', 'type', 'salary', 'remote', 'link']
        
        
class LanguageSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'languageid', 'name', 'jobid']