from rest_framework import serializers
from apiapp.models import Countries


class CountrieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Countries
        fields = ('id','name','capital')