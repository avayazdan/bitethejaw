from rest_framework import serializers
# from submissions.serializers import SubmissionSerializer
# from .models import User
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'password_repeat',
                  'email', 'display_picture', 'bio')
        # add extra validations via `extra_kwargs`
        # extra_kwargs = {
        #     'first_name': {'required': True},
        #     'last_name': {'required': True}
        # }

    # make sure email in DB is unique via `UniqueValidator`
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    # Use the built-in `validate_password` validator from Django
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password_repeat = serializers.CharField(write_only=True, required=True)

    # custom validation function
    def validate(self, attributes):
        """this validation runs after the validations of each field"""

        if attributes['password'] != attributes['password_repeat']:
            raise serializers.ValidationError(
                {"password": "Password fields don't match."})

        return attributes

    def create(self, data):
        """data is already validated at this point"""

        user = User.objects.create(
            username=data['username'],
            email=data['email'],
            display_picture=data['display_picture'],
            bio=data['bio'],
        )

        # Password has to be set via `set_password` in order to be hashed!
        user.set_password(data['password'])

        # save serialized user to DB
        user.save()

        # Uncomment these print statements to compare non-hashed password and hashed password
        print('unserialized password which arrived in JSON format from frontend',
              data['password'])
        print('password stored in DB', getattr(user, 'password'))

        # Alternative to `User.create`: Use `User.create_user` method
        # user = User.objects.create_user(
        #     data['username'],
        #     password=data['password'],
        #     first_name=data['first_name'],
        #     last_name=data['last_name'],
        #     email=data['email']
        # )

        return user

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "date_joined", "email", "bio", "display_picture")
        
        #choose only the fields that you want to contain in your model

# class PopulatedUserSerializer(UserSerializer):
#     user_submissions = SubmissionSerializer()
