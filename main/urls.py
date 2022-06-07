from django.urls import path

from main import views, music_player, chat

urlpatterns = [
    path('list/', views.SongListView.as_view()),
    path('categories/', views.CategoryView.as_view()),
    path('create/', views.SongCreateView.as_view()),
    # path('list/', views.SongListView.as_view()),
    path('detail/<int:pk>/', views.SongDetailView.as_view()),
    path('list/<int:pk>/like/', views.add_to_liked),
    path('list/<int:pk>/dislike/', views.remove_from_liked),

    path('list/<int:pk>/favourites/', views.add_to_favourite),
    path('list/<int:pk>/unfavourites/', views.remove_from_favourite),

    path('update/<int:pk>/', views.SongUpdateView.as_view()),
    path('delete/<int:pk>/', views.SongDeleteView.as_view()),

    path('reviews/', views.ReviewListCreateView.as_view()),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view()),
    # path('music_player/', views.music_player())
    # path('music_player/', views.ParsingView.as_view()),

]

