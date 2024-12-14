from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .models import *
from rest_framework.decorators import api_view
from .serializers import *
from django.utils import timezone
from django.db.models import Q
from .ai import filterComment, filterReply, checkCriticalIssue
# Create your views here.


def home(request):
    return HttpResponse('hello')




@api_view(['POST'])
def create_account_api(request):
    datas = request.data
    user_account = UserAccount.objects.all()
    if user_account.filter(userID = datas["userID"]).exists():
        return Response({"success": False, "message": "User id already exists"})
    else:
        user_serializer = UserAccountSerializer(data = datas)
        if user_serializer.is_valid():
            serializesss = UserAccount.objects.create( 
                userID = datas['userID'],
                userName = datas['userName'],
                firstName = datas['firstName'],
                lastName = datas['lastName'],
                age = datas['age'],
                email = datas['email'],
                address = datas['address'],
                docPhoto = datas['docPhoto'],
                userPhoto = datas['userPhoto'],
                character = datas['character'],
                
            )
            final_data = user_serializer.data
            return Response({  "success": True, "user": final_data,  "status": 200})
        else:
            return Response({"success": False})
    





@api_view(['POST'])
def getUser(request):
    datas = request.data
    user_account = UserAccount.objects.all()
    if user_account.filter(userID = datas['userID']):
        user_account = UserAccount.objects.filter( userID = datas['userID'] )
        user_serializer = UserAccountSerializer(user_account, many=True)
        return Response({"success":True, "data": user_serializer.data})
    else:
        return Response({"success":False})
    




@api_view(['POST'])
def issue_api(request):
    datas = request.data
    criticalIssue = checkCriticalIssue(request, datas)
    if criticalIssue == True:
        return Response({"success": False, "message": "Rejected! This issue is critical"})
    main_user = UserAccount.objects.get(userID = datas['issuedBy'])
    datas['issuedBy'] = main_user.id
    user_issue = UserIssue.objects.all()
    user_issue_serializer = UserIssueSerializer(data = datas)
    
    if user_issue_serializer.is_valid():
        user_issue = UserIssue.objects.create(
            issuedBy = main_user,
            title = datas['title'],
            description = datas['description'],
            preferredCharacter = datas['preferredCharacter'],
            gotRelation = datas['gotRelation'],
            private = datas['private'],
            createdAt = timezone.now()
        )
        return Response({"success": True, "data": user_issue_serializer.data})
    else:
        return Response({"success": False})
        




@api_view(['POST'])
def postIssueReply(request):
    data = request.data
    issueID = data['issueID']
    repliedBy = data['repliedBy']
    checkReply = filterReply(request, data)
    if checkReply == True:
        return Response({"success": False, "message": "Rejected! Your reply was abusive or not related to this issue"})
    try:
        user_account = UserAccount.objects.get(userID = repliedBy)
        user_issue = UserIssue.objects.get(id = issueID)
        data['repliedBy'] = user_account.id
        issue_reply_serialier = IssueReplySerializer(data = data)
        if issue_reply_serialier.is_valid():
            create_reply = IssueReply.objects.create(
                issueID = user_issue,
                repliedBy = user_account,
                message = data['message'],
                date = timezone.now()
            )
            issuse_data = issue_reply_serialier.data
            issuse_data['id'] = create_reply.id
            issuse_data['repliedBy'] = repliedBy
            issuse_data['date'] = create_reply.date
            return Response({ "success": True, "data": issuse_data})
        else:
            return Response({ "success": False, "data": issue_reply_serialier.errors})
    except Exception as e:
        return Response({ "success": False})


# -----------------------------------------------------------------------------------------



@api_view(['POST'])
def get_all_issues_api(request):
    data = request.data
    character = data['userID']
    if data["userID"] != "none-0":
        try:
            user_account = UserAccount.objects.filter(userID = character).first()
            user_issues = UserIssue.objects.filter(preferredCharacter=user_account.character).order_by("-id")
            all_issues = UserIssueSerializer(user_issues, many=True).data
            # Categorize issues into public and private
            categorized_issues = {
                "private_issues": [],
                "public_issues": []
            }
            for issue in all_issues:
                issuedBy = issue['issuedBy']
                user = UserAccount.objects.get(id=issuedBy)
                issue['userName'] = user.userName
                if issue.get('private', False):
                    categorized_issues["private_issues"].append(issue)
                    pReplycount = IssueReply.objects.filter(issueID = issue['id']).count()
                    issue['reply_count'] = pReplycount
                else: 
                    categorized_issues["public_issues"].append(issue)
                    comments = ParentComment.objects.filter(issueID = issue['id'])
                    issue['comments_count'] = len(comments)
            return Response({ "success":True, "data": categorized_issues})
        except Exception as e:
            return Response({ "success":False})
    else:
        try:
            user_account = UserAccount.objects.all()
            for user in user_account:
                user_issues = UserIssue.objects.all().order_by("-id")
                # Serialize the issues
                all_issues = UserIssueSerializer(user_issues, many=True).data
                # Categorize issues into public and private
                categorized_issues = {
                    "private_issues": [],
                    "public_issues": []
                }
                for issue in all_issues:
                    issuedBy = issue['issuedBy']
                    user = UserAccount.objects.get(id=issuedBy)
                    issue['issuedBy'] = user.userID
                    if issue.get('private', False):
                        categorized_issues["private_issues"].append(issue)
                        pReplycount = IssueReply.objects.filter(issueID = issue['id']).count()
                        issue['reply_count'] = pReplycount
                    else: 
                        categorized_issues["public_issues"].append(issue)
                        comments = ParentComment.objects.filter(issueID = issue['id'])
                        issue['comments_count'] = len(comments)
                return Response({ "success":True, "data": categorized_issues})
        except Exception as e:
            return Response({ "success":False})






@api_view(['POST'])
def buildRelation(request):
    datas = request.data
    try:
        issueUser = UserAccount.objects.get(userID = datas['issueUser'])
        suggestionUser = UserAccount.objects.get(userID = datas['suggestionUser'])
        datas['issueUser'] = issueUser.id
        datas['suggestionUser'] = suggestionUser.id
        relation_serializer = RelationSerializer(data = datas)
        if relation_serializer.is_valid():
            relation = Relation.objects.create(
                relationName = datas['relationName'],
                issueUser_id = datas['issueUser'],
                suggestionUser_id = datas['suggestionUser'],
                issueToken = datas['issueToken'],
                suggestionToken = datas['suggestionToken'],
                channel = datas['channel'],
            )
            # change issueUser and suggestionUser to their respective userIDs
            relation_data = relation_serializer.data
            relation_data['issueUser'] = issueUser.userID
            relation_data['suggestionUser'] = suggestionUser.userID
            return Response({"success": True, "relation": relation_data, })
        else:
            return Response({"success" : False, "error": relation_serializer.errors})
    except Exception as e:
        return Response({"success": False, "error": e})
        
    





@api_view(['POST'])
def postComment(request):
    data = request.data
    issueID = data['issueID']
    commentedBy = data['commentedBy']
    commentdata = data
    checkComment = filterComment(request, commentdata)
    if checkComment == True:
        return Response({"success": False, "message": "Rejected! Your comment was abusive or not related to this issue"})
    try:
        user_account = UserAccount.objects.get(userID = commentedBy)
        user_issue = UserIssue.objects.get(id = issueID)
        data['commentedBy'] = user_account.id
        parent_comment_serializer = ParentCommentSerializer(data = data)
        if parent_comment_serializer.is_valid():
            comment = ParentComment.objects.create(
                issueID = user_issue,
                commentedBy = user_account,
                message = data['message'],
                agree = data['agree'],
                disagree = data['disagree'],
                date = timezone.now()
            )
            comment_data = parent_comment_serializer.data
            comment_data['id'] = comment.id
            comment_data['commentedBy'] = commentedBy
            comment_data['date'] = comment.date
            return Response({ "success": True, "data": comment_data})
        else:
            return Response({ "success": False, "data": parent_comment_serializer.errors})
    except Exception as e:
        return Response({ "success": False})
   







@api_view(['POST'])
def postReComment(request):
    datas = request.data
    mainUser = UserAccount.objects.get(userID = datas["reCommentedBy"])
    datas["reCommentedBy"] = mainUser.id
    comment_reply_serializer = ReCommentSerializer(data = datas)
    if comment_reply_serializer.is_valid():
        comment_reply = CommentReply.objects.create(
            commentID_id = datas['commentID'],
            reCommentedBy_id = datas["reCommentedBy"],
            message = datas['message'],
            agree = datas['agree'],
            disagree = datas['disagree'],
            date = timezone.now()
        )
        return Response({"success": True, "data": comment_reply_serializer.data})
    else:
        return Response({"success" :False, "data": comment_reply_serializer.errors})





@api_view(['POST'])
def updateCommentAgree(request):
    data = request.data
    commentID = data["commentID"]
    change = data["change"]
    comment = ParentComment.objects.get(id = commentID)
    if change == "increase":
        comment.agree += 1
    else:
        comment.agree -= 1
    comment.save()
    return Response({"success": True})





@api_view(['POST'])
def updateReCommentAgree(request):
    data = request.data
    reCommentID = data["reCommentID"]
    change = data["change"]
    reComment = CommentReply.objects.get(id = reCommentID)
    if change == "increase":
        reComment.agree += 1
    else:
        reComment.agree -= 1
    reComment.save()
    return Response({"success": True})







@api_view(['POST'])
def getMyComments(request):
    data = request.data
    userID = data["userID"]
    if userID:
        try:
            user_account = UserAccount.objects.get(userID = userID)
            myComments = ParentComment.objects.filter(commentedBy=user_account.id).order_by("-id")
            myReComments = CommentReply.objects.filter(reCommentedBy=user_account.id).order_by("-id")
            myIssueReply = IssueReply.objects.filter(repliedBy=user_account.id).order_by("-id")
            comment_serializer = ParentCommentSerializer(myComments, many=True)
            recomment_serializer = ReCommentSerializer(myReComments, many=True)
            issue_reply_serializer = IssueReplySerializer(myIssueReply, many=True)
            datas = {
                    "comments": comment_serializer.data, 
                    "recomments": recomment_serializer.data, 
                    "issue_reply": issue_reply_serializer.data
                }
            for f in datas["comments"]:
                f["userName"] = UserAccount.objects.get(id=f["commentedBy"]).userName
            for f in datas["recomments"]:
                f["userName"] = UserAccount.objects.get(id=f["reCommentedBy"]).userName
            for f in datas["issue_reply"]:
                f["userName"] = UserAccount.objects.get(id=f["repliedBy"]).userName
            return Response({ "success":True, "data": datas})
        except Exception as e:
            return Response({ "success":False, "error": e})
    else:
        return Response({"success":False})




@api_view(['POST'])
def specificIssue(request):
    data = request.data
    specifiissue = UserIssue.objects.filter(id = data['issueID'])
    user_serializer = UserIssueSerializer(specifiissue, many=True)
    issueID = data['issueID']
    issue_reply = IssueReply.objects.filter(issueID = issueID)
    issue_reply_serializer = IssueReplySerializer(issue_reply, many=True)
    for issue in user_serializer.data:
        issue["userName"] = UserAccount.objects.get(id=issue["issuedBy"]).userName
        issue["reply"] = [x for x in issue_reply_serializer.data if x['issueID'] == issue['id']]
        comments = ParentComment.objects.filter(issueID=issue['id'])
        issue["comments"] = ParentCommentSerializer(comments, many=True).data
        issue["comments_count"] = len(issue["comments"])
        issue["reply_count"] = len(issue["reply"])

    for repl in issue["reply"]:
        repl["userName"] = UserAccount.objects.get(id=repl["repliedBy"]).userName
        repl["repliedBy"] = UserAccount.objects.get(id=repl["repliedBy"]).userID
    
    for comment in issue["comments"]:
        re_comments = CommentReply.objects.filter(commentID=comment['id'])
        comment["userName"] = UserAccount.objects.get(id=comment["commentedBy"]).userName
        comment["re_comments"] = ReCommentSerializer(re_comments, many=True).data
        if comment["re_comments"]:
            for reCom in comment["re_comments"]:
                reCom["userName"] = UserAccount.objects.get(id=reCom["reCommentedBy"]).userName
    return Response({"success": True, "issue": user_serializer.data})







@api_view(['POST'])
def getMyRelations(request):
    data = request.data
    userID = data["userID"]
    if userID:
        try:
            user_account = UserAccount.objects.get(userID = userID)
            myRelations = Relation.objects.filter(Q(issueUser_id=user_account.id) | Q(suggestionUser_id=user_account.id))
            user_serializer = RelationSerializer(myRelations, many=True)
            reData = user_serializer.data
            for f in reData:
                f["issueUser"]= userID
                f["suggestionUser"]= UserAccount.objects.get(id=f["suggestionUser"]).userID
                f["userName"] = user_account.userName
            return Response({"success":True, "data": reData})
        except UserAccount.DoesNotExist:
            return Response({"success": True, "data": []})
        except Relation.DoesNotExist:
            return Response({"success": True, "data": []})
        except Exception as e:
            return Response({"success": False, "data": []})
    else:
        return Response({"success":False})






   



