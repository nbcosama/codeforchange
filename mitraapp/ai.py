GEMINI_API_KEY= 'AIzaSyB3Ql-TZXHmk-FzT8adI8ELJxPvvjvqJX0'
import json
import google.generativeai as genai
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import *
from .serializers import *
from sambandhanewapp.serializers import *
from rest_framework.decorators import api_view
import string
import random
from rest_framework.response import Response
genai.configure(api_key=GEMINI_API_KEY)
# model (Gemini model)
model = genai.GenerativeModel("gemini-1.5-flash")







mydata = {
  "Stress & Anxiety": [
    {
      "problem": "I get panic when I see unknown people around me.",
      "causes": [
        "Fear of social interaction",
        "Low confidence"
      ],
      "solutions": [
        "Practice small social interactions daily.",
        "Build self-confidence through positive affirmations.",
        "Engage in meditation to calm your mind."
      ]
    },
    {
      "problem": "Every night I feel anxious and suffocated.",
      "causes": [
        "Overthinking",
        "Lack of emotional outlet"
      ],
      "solutions": [
        "Practice meditation or mindfulness techniques.",
        "Write down your thoughts in a journal before sleeping.",
        "Listen to calming music or white noise."
      ]
    }
  ],
  "Depression": [
    {
      "problem": "I lost my beloved brother and isolated myself for months.",
      "causes": [
        "Grief",
        "Emotional trauma"
      ],
      "solutions": [
        "Talk to a trusted friend or counselor about your feelings.",
        "Engage in activities that bring small joys, like gardening or art.",
        "Take small steps to rebuild social connections over time."
      ]
    },
    {
      "problem": "I feel depressed due to career uncertainties and financial issues.",
      "causes": [
        "High expectations",
        "Socio-economic pressures"
      ],
      "solutions": [
        "Create a step-by-step plan to manage finances effectively.",
        "Pursue skill development to enhance career opportunities.",
        "Seek emotional support from family or close friends."
      ]
    }
  ],
  "Societal Pressures": [
    {
      "problem": "Unacceptance of intercaste relationships by parents.",
      "causes": [
        "Traditional societal norms",
        "Fear of societal judgment"
      ],
      "solutions": [
        "Communicate openly with your parents about your feelings.",
        "Educate them on changing cultural values and mutual respect.",
        "Seek mediation from a neutral family member or counselor."
      ]
    },
    {
      "problem": "I want to become a businessman, but my family and neighbors don’t support me.",
      "causes": [
        "Lack of understanding about entrepreneurship",
        "Fear of financial risk"
      ],
      "solutions": [
        "Educate your family about your business ideas and potential benefits.",
        "Start small to minimize financial risk and build trust over time.",
        "Join a community of like-minded entrepreneurs for support."
      ]
    }
  ],
  "Academic Pressure": [
    {
      "problem": "Studying under pressure made me feel overwhelmed and anxious.",
      "causes": [
        "High parental expectations",
        "Fear of failure"
      ],
      "solutions": [
        "Practice time management and break study tasks into smaller chunks.",
        "Ensure 6-7 hours of sleep even during exams.",
        "Incorporate relaxation techniques like deep breathing into your routine."
      ]
    },
    {
      "problem": "I failed in exams multiple times and felt depressed.",
      "causes": [
        "Fear of disappointing parents",
        "Low self-esteem"
      ],
      "solutions": [
        "Create a consistent and achievable study schedule.",
        "Seek academic help from teachers or peers.",
        "Focus on progress rather than perfection."
      ]
    }
  ],
  "Relationship Issues": [
    {
      "problem": "When I was a teenager, my parents isolated me after discovering my relationship.",
      "causes": [
        "Strict parental control",
        "Lack of understanding of teenage emotions"
      ],
      "solutions": [
        "Reflect on your parents’ perspective and communicate calmly.",
        "Focus on building trust with them over time.",
        "Engage in constructive activities to rebuild your confidence."
      ]
    },
    {
      "problem": "I fell in love with someone that I shouldn't have had.",
      "causes": [
        "Emotional attachment",
        "Conflict with personal values"
      ],
      "solutions": [
        "Practice mindfulness to manage your emotions.",
        "Seek guidance from a trusted friend or counselor.",
        "Focus on self-growth and setting healthy boundaries."
      ]
    }
  ],
  "Coping Mechanisms": [
    {
      "problem": "I feel mood swings and frequent irritation.",
      "causes": [
        "Hormonal imbalances",
        "Stress from daily life"
      ],
      "solutions": [
        "Watch lighthearted content to uplift your mood.",
        "Engage in regular physical activity.",
        "Maintain a balanced diet and proper sleep schedule."
      ]
    },
    {
      "problem": "I couldn't sleep for days due to stress.",
      "causes": [
        "Overthinking",
        "High anxiety levels"
      ],
      "solutions": [
        "Establish a fixed bedtime routine.",
        "Avoid caffeine or heavy meals before sleep.",
        "Use relaxation techniques like guided imagery or soft music."
      ]
    }
  ]
}

conversation_memory = {}
user_data = {}
def generate_content_from_gemini(final_prompt, user_id, fnlprompt, createChatConv):
    try:
        #getting history of user
        history,_ = AllConversation.objects.get_or_create(userID=user_id, chatConversation_id=createChatConv.id)
        # Create a prompt that includes the conversation history
        history_prompt = "\n".join(json.loads(history.conversation)) if history.conversation else ""
        newHistory = [] + json.loads(history.conversation) if history.conversation else []
        # If not found in static data, call Gemini API to generate content
        response = model.generate_content(f"{final_prompt}\n Conversation history: {history_prompt} new prompt: {fnlprompt} max_tokens: 50")
        response_text = response.text
        # Update the conversation memory
        newHistory.append(f"Asked by User: {fnlprompt}")
        newHistory.append(f"Answer by you: {response_text}")
       
        
        # user, query, and answer
        user_data["prompt"] = fnlprompt
        user_data["User ID"] = user_id
        user_data["You"] = response_text
        
        if AllConversation.objects.filter(userID=user_id).exists():
            save_data = AllConversation.objects.get(userID=user_id)
            save_data.conversation = json.dumps(newHistory)
            save_data.userID = user_id
            save_data.save()
        else:
            save_data = AllConversation(userID=user_id, conversation=json.dumps(newHistory))
            save_data.save()
        save_data = AiConversation(userID=user_id, message=fnlprompt, conversation_id=createChatConv.id)
        save_data.save()
        return response_text  # Return the generated content from Gemini
    except Exception as e:
        return f"Error generating content: {str(e)}"  # Handle any errors gracefully






def random_string(length=15):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))


def createConversation(user_id):
    random = random_string()
    try:    
        user = UserAccount.objects.get(userID=user_id)
        getexisted = ChatConversation.objects.filter(userID_id=user.id)
        if getexisted.exists():
            return getexisted[0]
        else:
            conversation = ChatConversation.objects.create(
                userID_id = user.id,
                conversationID = random,
                created_at = timezone.now()
            )
            return conversation
    except Exception as e:
        return Response({'error': str(e)})




@api_view(['POST'])
def meroSathi(request):
    data = request.data
    user_id = data["userID"]
    fnlprompt = data["message"]
    createChatConv = createConversation(user_id)
    context_data = json.dumps(mydata) 
    final_prompt = (
        f"Suppose yourself as this: {context_data}. Answer according to the data."
        f"POLICY: If anyone asks about conversation history, respond that you are not allowed to share it."
        f"Keep responses concise (maximum 50 words) and answer like a good friend or well-wisher."
        f"If a question is out of the data's context, politely decline to answer, saying it’s beyond your knowledge."
        f"Remember any personal details shared by the user during this conversation and respond accordingly."
        f"Adapt your tone to match the user's language and emotions."
        f"Provide solutions or suggestions strictly based on the data user needed."
        f"Keep your responses engaging, natural, and personal—avoid sounding like a robot."
        f"Behave uniquely with each user and tailor responses to their input."
        f"Focus on providing clear and relatable answers while ensuring relevance to the user’s query."
        f"Never reveal that you are an AI model or share any information about the data."
        f"Act as a second person and maintain a conversational tone throughout the interaction."
        f"Respond differently to each user based on their queries and emotions."
    )

    # Generate the solution based on the user-provided prompt or static data
    answer = generate_content_from_gemini(final_prompt, user_id, fnlprompt, createChatConv)
    if answer:
        answer = answer.replace("\n", "")
        try:
            save_data = AiConversation(userID="AI", message=answer, conversation_id=createChatConv.id)
            save_data.save()
        except Exception as e:
            return Response({'message': 'User not found'})

    # loadchat = loadConversation(request, user_id)
    # Return the answer (either static or generated) as a JSON response
    # , 'answer': answer
    return JsonResponse({'chat':save_data.message,})




@api_view(['POST'])
def loadConversation(request):
    data = request.data
    userID = data["userID"]
    try:
        user = UserAccount.objects.get(userID = userID)
        chatConversation = ChatConversation.objects.get(userID = user)
        conversation = AiConversation.objects.filter(conversation = chatConversation)
        conversation_serializer = AiConversationSerializer(conversation, many=True)
        return Response({"success":True,"data": conversation_serializer.data})
    except Exception as e:
        return Response({"success":True,"data": []})
    



