from django.urls import path
from .views import UsersListView, UsersDetailView, RegisterView

urlpatterns = [
    path('', UsersListView.as_view()),
    path('register/', RegisterView.as_view()),
    path('<str:pk>/', UsersDetailView.as_view()),
]
