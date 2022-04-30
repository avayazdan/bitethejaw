from rest_framework import generics
from .models import Submissions
from .serializers import SubmissionSerializer

class SubmissionsListView(generics.ListCreateAPIView):
    queryset = Submissions.objects.all()
    serializer_class = SubmissionSerializer

class SubmissionsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Submissions.objects.all()
    serializer_class = SubmissionSerializer

