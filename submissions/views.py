from rest_framework import generics
from .models import Submissions
from .serializers import SubmissionSerializer
# from django.views.generic.edit import UpdateView


class SubmissionsListView(generics.ListCreateAPIView):
    queryset = Submissions.objects.all()
    serializer_class = SubmissionSerializer


class SubmissionsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Submissions.objects.all()
    serializer_class = SubmissionSerializer


# class SubmissionsUpdateView(UpdateView):
#     model = Submissions
#     fields = [
#         "image",
#         "text_field",
#         "category"
#     ]

#     success_url = "/"
