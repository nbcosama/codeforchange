from django.db import models
from sambandhanewapp.models import *



class StaticData(models.Model):
    collectedData = models.TextField()
    solution = models.TextField()
    



class ChatConversation(models.Model):
    conversationID = models.CharField(max_length=100, null=True, default="")
    userID = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="user")
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Conversation {self.conversationID}"




class AiConversation(models.Model):
    conversation = models.ForeignKey(ChatConversation, on_delete=models.CASCADE, related_name="messages", null=True, default="")
    userID = models.CharField(max_length=100, null=True, default="")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.userID





class AllConversation(models.Model):
    chatConversation = models.ForeignKey(ChatConversation, on_delete=models.CASCADE, null=True, default="")
    conversation = models.TextField()
    userID = models.CharField(max_length=100, null=True, default="")    
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.userID



