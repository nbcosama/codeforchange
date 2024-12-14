from django.urls import path
from . import views
from . import ai

urlpatterns = [
    path('meroSathi' , ai.meroSathi, name='meroSathi'),
    path('loadConversation', ai.loadConversation, name='loadConversation'),
]