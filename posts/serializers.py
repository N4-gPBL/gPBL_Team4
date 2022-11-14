from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    createdAt = serializers.DateTimeField()
    updatedAt = serializers.DateTimeField()
    content = serializers.CharField()
    summary = serializers.CharField()
    categoryId = serializers.IntegerField()
    slug = serializers.CharField()
    title = serializers.CharField()


    def __init__(self, instance=None, data=..., **kwargs):
        super().__init__(instance, data, **kwargs)
        self.fields['id'].read_only = True
        self.fields['createdAt'].required = False
        self.fields['updatedAt'].required = False

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.createdAt = validated_data.get('createdAt', instance.createdAt)
        instance.updatedAt = validated_data.get('updatedAt', instance.updatedAt)
        instance.content = validated_data.get('content', instance.content)
        instance.summary = validated_data.get('summary', instance.summary)
        instance.categoryId = validated_data.get('categoryId', instance.categoryId)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance


    def is_valid(self, *, raise_exception=False):
        if (self.initial_data['categoryId'] == None):
            raise serializers.ValidationError("categoryId is required")
        if (self.initial_data['slug'] == None):
            raise serializers.ValidationError("slug is required")
        if (self.initial_data['title'] == None):
            raise serializers.ValidationError("title is required")
        return super().is_valid(raise_exception=raise_exception)

    class Meta:
        model = Post
        fields = ('id', 'createdAt', 'updatedAt', 'content', 'summary', 'categoryId', 'slug', 'title')

    