from rest_framework import serializers
from rest_framework.serializers import ReadOnlyField, PrimaryKeyRelatedField, ModelSerializer

from main.models import Song, Category, Review


class SongSerializer(serializers.ModelSerializer):
    owner = ReadOnlyField(source='owner.email')
    reviews = PrimaryKeyRelatedField(many=True, read_only=True)


    class Meta:
        model = Song
        fields = '__all__'

    def is_liked(self, song):
        user = self.context.get('request').user
        return user.liked.filter(song=song).exists()

    def is_favourite(self, song):
        user = self.context.get('request').user
        return user.liked.filter(song=song).exists()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['reviews_detail'] = ReviewSerializer(instance.reviews.all(), many=True).data
        user = self.context.get('request').user
        if user.is_authenticated:
            representation['is_liked'] = self.is_liked(instance)
        if user.is_authenticated:
            representation['is_favourite'] = self.is_favourite(instance)
        representation['likes_count'] = instance.likes.count()
        return representation


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ReviewSerializer(ModelSerializer):
    owner = ReadOnlyField(source='owner.email')

    class Meta:
        model = Review
        fields = ('id', 'body', 'owner', 'song')


# class ParsingSerializer(serializers.ModelSerializer):


