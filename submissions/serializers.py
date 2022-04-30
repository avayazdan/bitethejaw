from ast import Sub
from rest_framework import serializers
from .models import Submissions
from users.models import User

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submissions
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

        def create(self, data):
            User_data = data.pop("user")

            User = User(**data)

            if User_data:
                User, _created = User.objects.get_or_create(
                    **User_data)
                Submissions.User = User

            # Need to save to get the id
            Submissions.save()

            return Submissions

    def update(self, submissions, data):
        User_data = data.pop("User")
        Submissions.image = data.get("image", Submissions.image)

        if User_data:
            User, _created = User.objects.get_or_create(
                **User_data)
            User.author = User
            
        # save to the database
        User.save()

        # render to the api
        return Submissions
