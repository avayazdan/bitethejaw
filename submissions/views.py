from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Submissions
from .serializers import SubmissionSerializer


class SubmissionsListView(APIView):
    # `_request` is not used. The leading underscore expresses that it won't be used.
    def get(self, _request):
        submissions = Submissions.objects.all()
        serialized_shows = SubmissionSerializer(submissions, many=True)
        return Response(serialized_shows.data)
