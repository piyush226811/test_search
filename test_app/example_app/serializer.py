from rest_framework import serializers

from .models import Country, Player, Blog


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
