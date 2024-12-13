from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(UserAccount)
admin.site.register(UserIssue)
admin.site.register(IssueReply)
admin.site.register(Relation)
admin.site.register(ParentComment)
admin.site.register(CommentReply)