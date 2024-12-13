from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(StaticData)
admin.site.register(ChatConversation)
admin.site.register(AiConversation)
admin.site.register(AllConversation)