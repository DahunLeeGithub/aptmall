from rest_framework import serializers
from .models import Item, Category, Post

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'category', 'thumbnail', 'created_date', 'published_date', 'price')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'body', 'id')