from rest_framework import serializers
from main.models import Song
from cart.models import Order


class OrderSerializer(serializers.Serializer):
    song = serializers.IntegerField()
    count = serializers.IntegerField()

    def validate(self, attrs):
        data = {}
        try:
            song = Song.objects.get(pk=attrs['song'])
        except Song.DoesNot.Exist:
            raise serializers.ValidationError('Failed to find the product')
        count = attrs['count']
        data['count'] = count
        data['song'] = song.pk
        return data

    def save(self, **kwargs):
        data = self.validated_data
        user = kwargs['user']
        song = Song.objects.get(pk=data['song'])
        Order.objects.create(
            song=song,
            user=user,
            count=data['count'],)