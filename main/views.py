from tkinter import mainloop

from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

# from rest_framework.generics import GenericAPIView

from main import serializers, music_player
from main.models import Song, Category, Review, Likes
from main.permissions import IsAuthor
from main.serializers import SongSerializer
# from main.music_player import a

from django_filters.rest_framework import DjangoFilterBackend



# import pygame
# from pygame import mixer
# from tkinter import *
# import os

class SongListView(APIView):

    def get(self, request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

class StandartPaginationClass(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000


class SongListView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = serializers.SongSerializer
    pagination_class = StandartPaginationClass
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('owner', 'category')
    search_fields = ('name',)

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
    song = Song.objects.get(id=pk)
    if request.user.liked.filter(song=song).exists():
        return Response('Вы уже лайкали данный пост', status=status.HTTP_400_BAD_REQUEST)
    Likes.objects.create(song=song, user=request.user)
    return Response('Добавлено в понравившийся', status=status.HTTP_201_CREATED)


@api_view(['POST'])
def remove_from_liked(request, pk):
    song = Song.objects.get(id=pk)
    if not request.user.liked.filter(song=song).exists():
        return Response('Данный пост отсутствует в списке понравившийся',status=status.HTTP_400_BAD_REQUEST)
    request.user.liked.filter(song=song).delete()
    return Response('Убрано из списка понравившийся', status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def add_to_favourite(request, pk):
    song = Song.objects.get(id=pk)
    if request.user.favourite.filter(song=song).exists():
        return Response('Этот пост у вас уже в Избранном', status=status.HTTP_400_BAD_REQUEST)
    Likes.objects.create(song=song, user=request.user)
    return Response('Добавлено в Избранные', status=status.HTTP_201_CREATED)


@api_view(['POST'])
def remove_from_favourite(request, pk):
    song = Song.objects.get(id=pk)
    if not request.user.favourite.filter(song=song).exists():
        return Response('Данный пост отсутствует в списке избранных',status=status.HTTP_400_BAD_REQUEST)
    request.user.liked.filter(song=song).delete()
    return Response('Убрано из списка избранных', status=status.HTTP_204_NO_CONTENT)


# class ParsingView(APIView):
#     def get(self, request):
#         parsing = mainloop()
#
#         # serializer = ParsingSerializer(instance = parsing, many=True)
#         return Response(parsing)
#
# class ChatView(APIView):
#     def get(self, request):
#         chat = chat()

# # music_player()
# def play(self):
#     self = a
#



#
# def playsong():
#     currentsong=playlist.get(ACTIVE)
#     print(currentsong)
#     mixer.music.load(currentsong)
#     songstatus.set("Playing")
#     mixer.music.play()
#
# def pausesong():
#     songstatus.set("Paused")
#     mixer.music.pause()
#
# def stopsong():
#     songstatus.set("Stopped")
#     mixer.music.stop()
#
# def resumesong():
#     songstatus.set("Resuming")
#     mixer.music.unpause()
#
# root=Tk()
# root.title('Music player project')
#
# mixer.init()
# songstatus=StringVar()
# songstatus.set("choosing")
#
# #playlist---------------
#
# playlist=Listbox(root,selectmode=SINGLE,bg="darkblue",fg="white",font=('arial',15),width=70, height=25)
# playlist.grid(columnspan=5)
#
# os.chdir(r'/home/hello/Desktop/music_player')
# songs=os.listdir()
# for s in songs:
#     playlist.insert(END,s)
#
# playbtn=Button(root,text="Play",command=playsong)
# playbtn.config(font=('arial',20),bg="darkblue",fg="white",padx=60,pady=14)
# playbtn.grid(row=1,column=0)
#
# pausebtn=Button(root,text="Pause",command=pausesong)
# pausebtn.config(font=('arial',20),bg="darkblue",fg="white",padx=60,pady=14)
# pausebtn.grid(row=1,column=1)
#
# stopbtn=Button(root,text="Stop",command=stopsong)
# stopbtn.config(font=('arial',20),bg="darkblue",fg="white",padx=60,pady=14)
# stopbtn.grid(row=1,column=2)
# #
# Resumebtn=Button(root,text="Resume",command=resumesong)
# Resumebtn.config(font=('arial',20),bg="darkblue",fg="white",padx=60,pady=14)
# Resumebtn.grid(row=1,column=3)
#
#
# mainloop()


