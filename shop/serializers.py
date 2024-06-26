from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Product, ProductImage, Comment, Rating, Editor, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['user',]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['password'] = make_password(user_data['password'])
        user = User.objects.create(**user_data)
        profile = Profile.objects.create(user=user, **validated_data)
        return profile


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = '__all__'

    def get_image_url(self, obj):
        return obj.image.image.url if obj.image else None


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class EditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editor
        fields = '__all__'





