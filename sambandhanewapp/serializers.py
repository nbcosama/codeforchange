from rest_framework import serializers
from .models import *


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = [ 'userID', 'userName', 'firstName', 'lastName', 'age', 'email', 'address', 'docPhoto', 'userPhoto', 'character', 'isVerified', 'createdAt', 'updatedAt']