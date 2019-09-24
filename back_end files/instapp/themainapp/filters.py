from django_filters import FilterSet, rest_framework
from .models import *


class UserFilter(FilterSet):
    class Meta:
        model = User
        exclude = ('Image', )


class ImagesFilter(FilterSet):
    class Meta:
        model = Images
        exclude = ('Image', )


class CommentsFilter(FilterSet):
    class Meta:
        model = Comments
        fields = '__all__'


class LikedFilter(FilterSet):
    class Meta:
        model = Liked
        fields = '__all__'

