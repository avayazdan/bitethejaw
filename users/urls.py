from django.urls import path
from .views import UsersListView, UsersDetailView

urlpatterns = [
    path('', UsersListView.as_view()),
    path('<str:pk>/', UsersDetailView.as_view())
]