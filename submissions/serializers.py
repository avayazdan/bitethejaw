from rest_framework import serializers
# from users.serializers import UserSerializer
from .models import Submissions
# from users.models import User
from django.contrib.auth import get_user_model


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submissions
        fields = '__all__'
        


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

User = serializers.SlugRelatedField(
  slug_field="username", read_only=True)

class PopulatedSubmissionSerializer(SubmissionSerializer):
    submitted_by = UserSerializer()


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

#         def create(self, data):
#             User_data = data.pop("user")

#             User = User(**data)
#             User.set_password(data['password'])
#             User.save()


#             if User_data:
#                 User, _created = User.objects.get_or_create(
#                     **User_data)
#                 Submissions.User = User

    # # Need to save to get the id
    # Submissions.save()

    # return Submissions

    # def update(self, Submissions, data):
    #     User_data = data.pop("User")
    #     Submissions.image = data.get("image", Submissions.image)

    #     if User_data:
    #         User, _created = User.objects.get_or_create(
    #             **User_data)
    #         User.author = User

    #     # save to the database
    #     User.save()

    #     # render to the api
    #     return Submissions
