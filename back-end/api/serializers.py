from django.contrib.auth.models import User
from django.db.models.query_utils import select_related_descend
from rest_framework import serializers
from api.models import NotWorkType, NotWorkingDay, Schedule, Sheet, SheetTitle, SheetValue
from rest_framework.permissions import AllowAny
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    # username_field = User.EMAIL_FIELD

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        # token['email'] = user.EMAIL_FIELD
        return token


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class NotWorkingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotWorkType
        fields = '__all__'
        read_only_fields = ['id']


class NotWorkingDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = NotWorkingDay
        fields = (
            'id',
            'sheet',
            'description',
            'day',
        )
        read_only_fields = ['id']


class TitlesFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SheetTitle
        fields = '__all__'
        read_only_fields = ['id']


class ValuesFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SheetValue
        fields = '__all__'
        read_only_fields = ['id', 'user']


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'
        read_only_fields = ['id']


class SheetSerializer(serializers.ModelSerializer):
    titles_fields = serializers.StringRelatedField()
    values_fields = ValuesFieldsSerializer()

    class Meta:
        model = Sheet
        fields = (
            'user',
            'date',
            'titles_fields',
            'values_fields',
            'schedule',
            'title',
            'img_path',
        )
        read_only_fields = ['id', 'user']
