from rest_framework.response import Response
from .serializers import *
from .models import *


def get_issue_reply(request, issuedBy):
    issue = UserIssue.objects.filter(issuedBy = issuedBy)
    data = []
    for i in issue:
        issue_reply = IssueReply.objects.all()
        if issue_reply.filter(issueID = i.id).exists():
            issue_reply = IssueReply.objects.filter(
                issueID = i.id
            )
            issue_reply_serializer = IssueReplySerializer(issue_reply, many=True)
            for iss in issue_reply_serializer.data:
                data.append(iss)
    return data
        

# public comment
