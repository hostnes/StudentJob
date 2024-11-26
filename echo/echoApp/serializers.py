from rest_framework import serializers
from .models import (
    Country, Region, District, Messenger, Education, User, Company,
    Vacancy, Comment, Summary, Response
)

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'title']

class RegionSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = Region
        fields = ['id', 'title', 'country']

class DistrictSerializer(serializers.ModelSerializer):
    region = RegionSerializer()

    class Meta:
        model = District
        fields = ['id', 'title', 'region']

class MessengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messenger
        fields = ['id', 'title', 'url', 'is_publish']

class EducationSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = Education
        fields = ['id', 'title', 'country']

class UserSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    region = RegionSerializer()
    district = DistrictSerializer()
    place_of_education = EducationSerializer()

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'email', 'username', 'phone', 'gender',
            'img', 'birthday', 'country', 'region', 'district', 'place_of_education',
            'publish_phone', 'public_status'
        ]

class CompanySerializer(serializers.ModelSerializer):
    creator = UserSerializer()
    country = CountrySerializer()

    class Meta:
        model = Company
        fields = ['id', 'title', 'logo', 'description', 'creator', 'country']

class VacancySerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    region = RegionSerializer()
    district = DistrictSerializer()
    company = CompanySerializer()

    class Meta:
        model = Vacancy
        fields = [
            'id', 'title', 'description', 'salary', 'currency', 'date_of_create',
            'responses', 'country', 'region', 'district', 'company',
            'experience', 'education', 'employment', 'is_publish'
        ]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'photo', 'user', 'text']

class SummarySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Summary
        fields = [
            'id', 'title', 'description', 'date_of_create', 'user',
            'experience', 'education', 'employment', 'is_publish'
        ]

class ResponseSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    vacancy = VacancySerializer()

    class Meta:
        model = Response
        fields = ['id', 'user', 'vacancy', 'message']
