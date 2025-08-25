# users/serializers.py
from django.contrib.auth import get_user_model, password_validation
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    """
    Create a user with a properly hashed password and expose join/login timestamps.
    """
    password = serializers.CharField(write_only=True, trim_whitespace=False)
    password2 = serializers.CharField(write_only=True, trim_whitespace=False)

    class Meta:
        model = User
        fields = (
            "id", "username", "email",
            "password", "password2",
            "date_joined", "last_login",
        )
        read_only_fields = ("id", "date_joined", "last_login")

    def validate(self, attrs):
        # passwords match?
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Passwords do not match."})

        # optional: enforce unique email (remove if you don’t want this)
        email = attrs.get("email")
        if email and User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError({"email": "Email already in use."})

        # run Django’s password validators (length, common passwords, etc.)
        password_validation.validate_password(attrs["password"])
        return attrs

    def create(self, validated_data):
        # extract and hash password, discard password2
        password = validated_data.pop("password")
        validated_data.pop("password2", None)
        # create_user handles hashing + defaults
        user = User.objects.create_user(password=password, **validated_data)
        return user


class MeSerializer(serializers.ModelSerializer):
    """
    Read/update the current user. Exposes timestamps as read-only.
    """
    class Meta:
        model = User
        fields = ("id", "username", "email", "is_staff", "date_joined", "last_login")
        read_only_fields = ("id", "is_staff", "date_joined", "last_login")


class ChangePasswordSerializer(serializers.Serializer):
    """
    Change the current user’s password safely with validation.
    """
    old_password = serializers.CharField(write_only=True, trim_whitespace=False)
    new_password = serializers.CharField(write_only=True, trim_whitespace=False)
    new_password2 = serializers.CharField(write_only=True, trim_whitespace=False)

    def validate(self, attrs):
        user = self.context["request"].user

        # verify old password
        if not user.check_password(attrs["old_password"]):
            raise serializers.ValidationError({"old_password": "Incorrect password."})

        # match + validate new password
        if attrs["new_password"] != attrs["new_password2"]:
            raise serializers.ValidationError({"new_password": "Passwords do not match."})

        password_validation.validate_password(attrs["new_password"], user)
        return attrs

    def save(self, **kwargs):
        user = self.context["request"].user
        user.set_password(self.validated_data["new_password"])
        user.save()
        return user
