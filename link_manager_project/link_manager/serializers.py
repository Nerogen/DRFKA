from rest_framework import serializers
from .models import Link, Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'description', 'created_at', 'updated_at']


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'collection', 'title', 'description', 'url', 'image', 'created_at', 'updated_at']
