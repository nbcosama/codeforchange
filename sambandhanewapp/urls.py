from django.urls import path
from . import views
from . import ai    


urlpatterns = [
    path('', views.home, name='home'),
    path('create_account_api' , views.create_account_api, name='create_account_api'),
    path('getUser', views.getUser, name='getUser'),
    path('issue_api', views.issue_api, name='issue_api'),
    path('postIssueReply', views.postIssueReply, name='postIssueReply'),
    path('get_all_issues_api', views.get_all_issues_api, name='get_all_issues_api'),
    path('buildRelation', views.buildRelation, name='buildRelation'),
    path('postComment', views.postComment, name='postComment'),
    path('postReComment', views.postReComment, name='postReComment'),
    path('specificIssue', views.specificIssue, name='specificIssue'),
    path('getMyRelations', views.getMyRelations, name='getMyRelations'),
    path('updateCommentAgree', views.updateCommentAgree, name='updateCommentAgree'),
    path('updateReCommentAgree', views.updateReCommentAgree, name='updateReCommentAgree'),
    path('getMyComments', views.getMyComments, name='getMyComments'),
    path('filterIssueCategory', ai.filterIssueCategory, name='filterIssueCategory'),

]



