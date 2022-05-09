from django.urls import path
from .views import SubmissionsDetailView, SubmissionsListView
# from .views import SubmissionsUpdateView

urlpatterns = [
    path('', SubmissionsListView.as_view()),
    # path('new/', SubmissionsCreateView.as_view()),
    path('<int:pk>/', SubmissionsDetailView.as_view())
]