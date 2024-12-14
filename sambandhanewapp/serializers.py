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





class RelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relation
        fields = ['id', 'relationName', 'issueUser', 'suggestionUser', 'issueToken', 'suggestionToken', 'channel', 'createdAt']







class ParentCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentComment
        fields = ['id', 'issueID', 'commentedBy', 'message', 'agree', 'disagree', 'date' ]








class ReCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentReply
        fields = ['id', 'commentID', 'reCommentedBy', 'message', 'agree', 'disagree', 'date']






class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'type', 'typeID', 'reportedBy', 'message', 'status', 'createdAt', 'updatedAt']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'reportedBy', 'message', 'createdAt', 'updatedAt']