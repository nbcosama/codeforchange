from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserAccount(models.Model):
    CHARACTER_CHOICES = [
                ('father', 'Father'),
                ('mother', 'Mother'),
                ('son', 'Son'),
                ('teacher', 'Teacher'),
                ('student', 'Student'),
                ('uncle', 'Uncle'),
                ('sister', 'Sister'),
                ('brother', 'Brother'),
                ('daughter', 'Daughter'),
    ]

    userID = models.CharField(max_length=100)
    userName  = models.CharField(max_length=100, null=True, default="")
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=100, null=True, default="" )
    docPhoto = models.TextField(null=True, default="")
    userPhoto = models.TextField(null=True, default="")
    character = models.CharField(max_length=100, choices=CHARACTER_CHOICES)
    isVerified = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.userID
   
    




class UserIssue(models.Model):
        CHARACTERFIELD = [
               ('father', 'Father'),
                ('mother', 'Mother'),
                ('son', 'Son'),
                ('teacher', 'Teacher'),
                ('student', 'Student'),
                ('uncle', 'Uncle'),
                ('sister', 'Sister'),
                ('brother', 'Brother'),
                ('daughter', 'Daughter'),

                ]   
        issuedBy  = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
        title = models.CharField(max_length=100)
        description = models.TextField()
        preferredCharacter = models.CharField(max_length=100, choices=CHARACTERFIELD)
        gotRelation  = models.BooleanField(default=False)
        private = models.BooleanField(default=True)
        createdAt = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        def __str__(self):
            return self.title
        
        

    


class IssueReply(models.Model):
    issueID = models.ForeignKey(UserIssue, on_delete=models.CASCADE)
    repliedBy = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.message
    
    



class Relation(models.Model):
    relationName = models.CharField(max_length=255, default="relation")
    issueToken = models.CharField(max_length=255, default="")
    suggestionToken = models.CharField(max_length=255, default="")
    channel = models.JSONField(null=True)
    issueUser = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='issued_by')
    suggestionUser = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='suggested_by')
    createdAt = models.DateTimeField(auto_now_add=True)
    def _str_(self): 
        return self.issueToken



class ParentComment(models.Model):
    issueID = models.ForeignKey(UserIssue, on_delete=models.CASCADE)
    commentedBy = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    message = models.TextField()
    agree = models.IntegerField( null=True, default="" ) 
    disagree = models.IntegerField( null=True, default="" )
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.commentedBy.firstName
    


class CommentReply(models.Model):
    commentID = models.ForeignKey(ParentComment, on_delete=models.CASCADE)
    reCommentedBy = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    message = models.TextField()
    agree = models.IntegerField( null=True, default="" ) 
    disagree = models.IntegerField( null=True, default="" )
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.message
    




class Report(models.Model):
    REPORTYPE = [
        ('issue', 'Issue'),
        ('reply', 'Reply'),
        ('comment', 'Comment'),
        ('reComment', 'Re-Comment'),
        ('mitra', 'Mitra'),
    ]
    type = models.CharField(max_length=100, choices=REPORTYPE)

    typeID = models.CharField(max_length=50, null=True, blank=True)  # Keep it simple for ID storage

    reportedBy = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    message = models.TextField()
    status =  models.CharField(max_length=100, default="pending")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def _str_(self):
        return f"{self.message} -- {self.status}"


        
    


class Feedback(models.Model):
    reportedBy = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    message = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def _str_(self):
        return f"{self.message} -- {self.createdAt}"