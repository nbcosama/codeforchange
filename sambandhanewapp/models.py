from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserAccount(models.Model):
    CHARACTER_CHOICES = [
                ('father', 'Father'),
                ('mother', 'Mother'),
                ('son', 'Son'),
                ('daughter', 'Daughter'),
                ('teacher', 'Teacher'),
                ('student', 'Student'),
                ('uncle', 'Uncle'),
                ('brother', 'brother'),
                ('sister', 'sister'),
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
    def __save__(self):
        self.updated_at = timezone.now()
        return super().save()
    




class UserIssue(models.Model):
        CHARACTERFIELD = [
                ('father', 'Father'),
                ('mother', 'Mother'),
                ('son', 'Son'),
                ('daughter', 'Daughter'),
                ('grandfather', 'Grandfather'),
                ('grandmother', 'Grandmother'),
                ('uncle', 'Uncle'),

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
        def __save__(self):
            self.updated_at = timezone.now()
            return super().save()
        

    

