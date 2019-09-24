from rest_framework import serializers
from .models import User, Liked, Images, Comments
from drf_extra_fields.fields import Base64ImageField
from rest_framework.decorators import action


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'phone_number', 'email', 'address', 'Image']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        group = validated_data.pop('groups', None)
        validated_data.pop('user_permissions', None)
        k = User.objects.create_user(**validated_data)
        k.save()
        return k


class ImageSerializer(serializers.ModelSerializer):
    person_uploaded_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source="person_uploaded", write_only=True)
    person_uploaded = UserSerializer(read_only=True)
    Image = Base64ImageField()
    liked_or_not = serializers.SerializerMethodField()

    class Meta:
        model = Images
        fields = '__all__'

    def get_liked_or_not(self, data):
        qs = Liked.objects.filter(ImageId=data, personId=self.context["request"].user).first()
        if qs:
            return True
        else:
            return False


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


class LikedSerializer(serializers.ModelSerializer):
    personId = UserSerializer(read_only=True)

    class Meta:
        model = Liked
        fields = '__all__'

