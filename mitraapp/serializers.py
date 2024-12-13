from rest_framework import serializers
from .models import *

class ChatConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatConversation
        fields = ['id', 'conversationID', 'userID', 'created_at']




class AiConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AiConversation
        fields = ['id', 'conversation', 'userID', 'message', 'created_at']

