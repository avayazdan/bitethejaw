from rest_framework import generics
from .models import Submissions
from .serializers import SubmissionSerializer
from rest_framework.permissions import IsAuthenticated
# from django.views.generic.edit import UpdateView


class SubmissionsListView(generics.ListAPIView):
    queryset = Submissions.objects.all()
    serializer_class = SubmissionSerializer


class SubmissionsCreateView(generics.CreateAPIView):
    queryset = Submissions.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = (IsAuthenticated,)


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
