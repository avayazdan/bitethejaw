from rest_framework import generics
from .models import Submissions
from .serializers import SubmissionSerializer, PopulatedSubmissionSerializer
from rest_framework.permissions import IsAuthenticated
from users.models import User
# from django.views.generic.edit import UpdateView


class SubmissionsListView(generics.ListAPIView):
    queryset = Submissions.objects.all()
    serializer_class = PopulatedSubmissionSerializer


class SubmissionsCreateView(generics.CreateAPIView):
    queryset = Submissions.objects.all()
    serializer_class = PopulatedSubmissionSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data["submitted_by"] = User.objects.get(username=request.user)
        serializer = self.serializer_class(
            data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()


class SubmissionsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Submissions.objects.all()
    serializer_class = PopulatedSubmissionSerializer


# class SubmissionsUpdateView(UpdateView):
#     model = Submissions
#     fields = [
#         "image",
#         "text_field",
#         "category"
#     ]

#     success_url = "/"
