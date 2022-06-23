from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=('id','title','description')