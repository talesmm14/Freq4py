from rest_framework import serializers
from api.models import Sheet

class Sheet_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Sheet
        fiedls = '__all__'