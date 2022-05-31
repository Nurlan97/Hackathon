from django.urls import path

from main import views

urlpatterns = [
    path('list/', views.SongListView.as_view()),
    path('categories/', views.CategoryView.as_view()),
    path('create/', views.SongCreateView.as_view()),
    # path('list/', views.SongListView.as_view()),
    path('detail/<int:pk>/', views.SongDetailView.as_view()),
    path('list/<int:pk>/like/', views.add_to_liked),
    path('list/<int:pk>/dislike/', views.remove_from_liked),
    path('update/<int:pk>/', views.SongUpdateView.as_view()),
    path('delete/', views.SongDeleteView.as_view()),

    path('reviews/', views.ReviewListCreateView.as_view()),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view()),
]

