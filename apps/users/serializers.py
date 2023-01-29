from rest_framework import serializers

from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'alias',
            'first_name',
            'last_name',
            'email',
            'password',
        )

    def create(self, validated_data):
        if not validated_data['password']:
            raise serializers.ValidationError('Password can\'t be blank!')
        validated_data.remove()
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    alias = serializers.CharField(
        write_only=True
    )
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label="Token",
        read_only=True
    )

    def validate(self, attrs):
        alias = attrs.get('alias')
        password = attrs.get('password')

        if alias and password:
            user = authenticate(request=self.context.get('request'), alias=alias, password=password)
            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs
