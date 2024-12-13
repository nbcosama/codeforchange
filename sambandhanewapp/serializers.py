from rest_framework import serializers
from .models import *


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = [ 'userID', 'userName', 'firstName', 'lastName', 'age', 'email', 'address', 'docPhoto', 'userPhoto', 'character', 'isVerified', 'createdAt', 'updatedAt']


class UserIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserIssue
        fields = [ 'id', 'issuedBy', 'title', 'description', 'preferredCharacter', 'gotRelation', 'private', 'createdAt']



class IssueReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueReply
        fields = ['id', 'issueID', 'repliedBy', 'message', 'date']

