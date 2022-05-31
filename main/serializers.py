from rest_framework import serializers
from rest_framework.serializers import ReadOnlyField, PrimaryKeyRelatedField, ModelSerializer

from main.models import Song, Category, Review


class SongSerializer(serializers.ModelSerializer):
    owner = ReadOnlyField(source='owner.username')
    recalls = PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Song
        fields = '__all__'

    def is_liked(self, song):
        user = self.context.get('request').user
        return user.liked.filter(song=song).exists()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['recalls_detail'] = ReviewSerializer(instance.recalls.all(), many=True).data
        user = self.context.get('request').user
        if user.is_authenticated:
            representation['is_liked'] = self.is_liked(instance)
        representation['likes_count'] = instance.likes.count()
        return representation


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ReviewSerializer(ModelSerializer):
    owner = ReadOnlyField(source='owner.username')

    class Meta:
        model = Review
        fields = ('id', 'body', 'owner', 'product')

