from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .models import *
from rest_framework.decorators import api_view
from .serializers import *
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
        