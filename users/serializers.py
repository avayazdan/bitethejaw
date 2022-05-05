from rest_framework import serializers
# from submissions.serializers import SubmissionSerializer
# from .models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "submissions", "date_joined", "email", "bio", "display_picture")
        
        #choose only the fields that you want to contain in your model

# class PopulatedUserSerializer(UserSerializer):
#     user_submissions = SubmissionSerializer()
