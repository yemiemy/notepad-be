from django.urls import path

from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('notes/', views.NoteListCreateAPIView.as_view()),
    path('notes/<int:pk>/', views.NoteRetrieveUpdateDestroyAPIView.as_view())
]