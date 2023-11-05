from faker import Faker

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

User = get_user_model()


class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate_email(self, email):
        if '@' not in email:
            raise serializers.ValidationError("Enter a valid email address")

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email address already in use")
        return email

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Passwords do not match")

        validate_password(data["password"])

        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)

        fake = Faker()
        username = fake.user_name().capitalize()

        while User.objects.filter(username=username).exists():
            username = fake.user_name()

        validated_data["username"] = username

        user = User.objects.create_user(**validated_data, is_active=True)
        return user


class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            raise serializers.ValidationError({"bad_token": _("Token is invalid or expired")})
