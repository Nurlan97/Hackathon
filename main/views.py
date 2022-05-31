from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from main import serializers
from main.models import Song, Category, Review, Likes
from main.permissions import IsAuthor
from main.serializers import SongSerializer

from django_filters.rest_framework import DjangoFilterBackend

# class SongListView(APIView):
#
#     def get(self, request):
#         songs = Song.objects.all()
#         serializer = SongSerializer(songs, many=True)
#         return Response(serializer.data)

class StandartPaginationClass(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000


class SongListView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = serializers.SongSerializer
    pagination_class = StandartPaginationClass
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('owner',)
    search_fields = ('title',)

class SongDetailView(generics.RetrieveAPIView):
    queryset = Song.objects.all()
    serializer_class = serializers.SongSerializer



class CategoryView(APIView):

    def get(self, request):
        name = Category.objects.all()
        serializer = SongSerializer(name, many=True)
        return Response(serializer.data)



class SongCreateView(generics.CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = serializers.SongSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SongUpdateView(generics.UpdateAPIView):
    queryset = Song.objects.all()
    serializer_class = serializers.SongSerializer


class SongDeleteView(generics.DestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = serializers.SongSerializer


class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAuthor, )

@api_view(['POST'])
def add_to_liked(request, pk):
    product = Song.objects.get(id=pk)
    if request.user.liked.filter(product=product).exists():
        return Response('Вы уже лайкали данный пост', status=status.HTTP_400_BAD_REQUEST)
    Likes.objects.create(product=product, user=request.user)
    return Response('Добавлено в понравившийся', status=status.HTTP_201_CREATED)


@api_view(['POST'])
def remove_from_liked(request, pk):
    product = Song.objects.get(id=pk)
    if not request.user.liked.filter(product=product).exists():
        return Response('Данный пост отсутствует в списке понравившийся',status=status.HTTP_400_BAD_REQUEST)
    request.user.liked.filter(product=product).delete()
    return Response('Убрано из списка понравившийся', status=status.HTTP_204_NO_CONTENT)

