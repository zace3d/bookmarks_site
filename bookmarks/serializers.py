from rest_framework import serializers
from .models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Bookmark
        fields = ('url', 'title', 'description', 'is_public', 'date_created', 'date_updated', 'owner', 'tags')