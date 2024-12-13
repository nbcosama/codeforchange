GEMINI_API_KEY= 'AIzaSyB3Ql-TZXHmk-FzT8adI8ELJxPvvjvqJX0'
import google.generativeai as genai
from .models import *
from .serializers import *
from sambandhanewapp.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
genai.configure(api_key=GEMINI_API_KEY)
# model (Gemini model)
model = genai.GenerativeModel("gemini-1.5-flash")





def filterComment(request, comment):
    comment = comment
    try:
        response = model.generate_content(f"Is the following comment abusive in any language? {comment} Answer only with 'yes' or 'no'.")
        response_text = response.text.strip().lower()
        if response_text == 'yes':
            return  True
        return False
    except Exception as e:
        return Response({'error': str(e)})





@api_view(['POST'])
def filterIssueCategory(request):
    data = request.data
    userID = data.get("userID")
    allIssues = UserIssue.objects.filter(issuedBy__userID=userID)
    issueSerialize = UserIssueSerializer(allIssues, many=True)
    allIssue = issueSerialize.data

    issueCategory = [
        'relationship',
        'stress and anxiety',
        'depression',
        'societal pressures',
        'academic pressure',
        'family pressure',
        'study pressure',
        'career pressure',
        'work stress',
        'financial pressure',
        'health pressure',
        'other',
    ]

    try:
        prompt = (
            "You are tasked with analyzing user issues and determining which category they fall into. "
            f"You are provided a list of issues reported by a user in JSON format: {allIssue}. "
            "Your goal is to identify the category that occurs the most frequently in the given issues. "
            f"Choose the category that has the highest frequency from the following list: {issueCategory}. "
            "If no issue matches a given category, return 'Other'. Your response should be only the category name from the given list or 'Other'."
        )
        response = model.generate_content(prompt)
        response_text = response.text.strip()

        if response_text:
            return Response({'issueCategory': response_text})
        return Response({'issueCategory': "Other"})
    except Exception as e:
        return Response({'issueCategory': False})
