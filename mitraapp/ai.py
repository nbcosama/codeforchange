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







# mydata = {
#   "Stress & Anxiety": [
#     {
#       "problem": "I get panic when I see unknown people around me.",
#       "causes": [
#         "Fear of social interaction",
#         "Low confidence"
#       ],
#       "solutions": [
#         "Practice small social interactions daily.",
#         "Build self-confidence through positive affirmations.",
#         "Engage in meditation to calm your mind."
#       ]
#     },
#     {
#       "problem": "Every night I feel anxious and suffocated.",
#       "causes": [
#         "Overthinking",
#         "Lack of emotional outlet"
#       ],
#       "solutions": [
#         "Practice meditation or mindfulness techniques.",
#         "Write down your thoughts in a journal before sleeping.",
#         "Listen to calming music or white noise."
#       ]
#     }
#   ],
#   "Depression": [
#     {
#       "problem": "I lost my beloved brother and isolated myself for months.",
#       "causes": [
#         "Grief",
#         "Emotional trauma"
#       ],
#       "solutions": [
#         "Talk to a trusted friend or counselor about your feelings.",
#         "Engage in activities that bring small joys, like gardening or art.",
#         "Take small steps to rebuild social connections over time."
#       ]
#     },
#     {
#       "problem": "I feel depressed due to career uncertainties and financial issues.",
#       "causes": [
#         "High expectations",
#         "Socio-economic pressures"
#       ],
#       "solutions": [
#         "Create a step-by-step plan to manage finances effectively.",
#         "Pursue skill development to enhance career opportunities.",
#         "Seek emotional support from family or close friends."
#       ]
#     }
#   ],
#   "Societal Pressures": [
#     {
#       "problem": "Unacceptance of intercaste relationships by parents.",
#       "causes": [
#         "Traditional societal norms",
#         "Fear of societal judgment"
#       ],
#       "solutions": [
#         "Communicate openly with your parents about your feelings.",
#         "Educate them on changing cultural values and mutual respect.",
#         "Seek mediation from a neutral family member or counselor."
#       ]
#     },
#     {
#       "problem": "I want to become a businessman, but my family and neighbors don’t support me.",
#       "causes": [
#         "Lack of understanding about entrepreneurship",
#         "Fear of financial risk"
#       ],
#       "solutions": [
#         "Educate your family about your business ideas and potential benefits.",
#         "Start small to minimize financial risk and build trust over time.",
#         "Join a community of like-minded entrepreneurs for support."
#       ]
#     }
#   ],
#   "Academic Pressure": [
#     {
#       "problem": "Studying under pressure made me feel overwhelmed and anxious.",
#       "causes": [
#         "High parental expectations",
#         "Fear of failure"
#       ],
#       "solutions": [
#         "Practice time management and break study tasks into smaller chunks.",
#         "Ensure 6-7 hours of sleep even during exams.",
#         "Incorporate relaxation techniques like deep breathing into your routine."
#       ]
#     },
#     {
#       "problem": "I failed in exams multiple times and felt depressed.",
#       "causes": [
#         "Fear of disappointing parents",
#         "Low self-esteem"
#       ],
#       "solutions": [
#         "Create a consistent and achievable study schedule.",
#         "Seek academic help from teachers or peers.",
#         "Focus on progress rather than perfection."
#       ]
#     }
#   ],
#   "Relationship Issues": [
#     {
#       "problem": "When I was a teenager, my parents isolated me after discovering my relationship.",
#       "causes": [
#         "Strict parental control",
#         "Lack of understanding of teenage emotions"
#       ],
#       "solutions": [
#         "Reflect on your parents’ perspective and communicate calmly.",
#         "Focus on building trust with them over time.",
#         "Engage in constructive activities to rebuild your confidence."
#       ]
#     },
#     {
#       "problem": "I fell in love with someone that I shouldn't have had.",
#       "causes": [
#         "Emotional attachment",
#         "Conflict with personal values"
#       ],
#       "solutions": [
#         "Practice mindfulness to manage your emotions.",
#         "Seek guidance from a trusted friend or counselor.",
#         "Focus on self-growth and setting healthy boundaries."
#       ]
#     }
#   ],
#   "Coping Mechanisms": [
#     {
#       "problem": "I feel mood swings and frequent irritation.",
#       "causes": [
#         "Hormonal imbalances",
#         "Stress from daily life"
#       ],
#       "solutions": [
#         "Watch lighthearted content to uplift your mood.",
#         "Engage in regular physical activity.",
#         "Maintain a balanced diet and proper sleep schedule."
#       ]
#     },
#     {
#       "problem": "I couldn't sleep for days due to stress.",
#       "causes": [
#         "Overthinking",
#         "High anxiety levels"
#       ],
#       "solutions": [
#         "Establish a fixed bedtime routine.",
#         "Avoid caffeine or heavy meals before sleep.",
#         "Use relaxation techniques like guided imagery or soft music."
#       ]
#     }
#   ]
# }



mydata = {
  "Student-Challenges": [
    {
      "problem": "I was so stressed because I failed in my math exam. My parents were already angry because I didn’t study properly, and I was scared they would not allow me to go on the school trip with my friends.",
      "solution": "I told myself I can’t change the past, so I started studying math every day for at least 2 hours. I also asked my math teacher for extra help, and she explained the topics clearly. After one month, I improved a lot and passed in the re-exam! My parents were happy and even let me go on the trip."
    },
    {
      "problem": "I was scared to speak in front of the class. Every time I had to give a presentation, my hands would shake, and I’d forget everything. My teacher scolded me for not preparing, but the truth was, I was too nervous to even try.",
      "solution": "One day, I decided to try something crazy. I stood in front of a mirror and gave my presentation to myself, pretending I was the audience. Then, I started recording myself on my phone while practicing. I cringed so hard watching it but made small changes each time. By the day of the presentation, I wasn’t perfect, but I made it through without freezing. Now, I still get nervous, but I know I can handle it!"
    },
    {
      "problem": "My parents couldn’t afford to buy me a new phone, even though I needed it for online classes. My old phone was so slow it would crash during important sessions, and I felt embarrassed to even ask for help.",
      "solution": "I didn’t want to ask my parents again, so I borrowed my cousin’s phone for a few days and started taking online surveys and small freelancing gigs. It wasn’t much, but after a few months, I saved enough to get a second-hand phone that worked fine. It felt so good to solve my problem on my own!"
    },
    {
      "problem": "My best friend stopped talking to me because I accidentally shared something personal about them in the group chat. I apologized, but they said they couldn’t trust me anymore.",
      "solution": "Instead of just apologizing again, I made a scrapbook of all our best moments together, like photos, silly memories, and even some inside jokes we shared. I gave it to them as a gift and wrote a heartfelt note saying how much I missed them. It took a while, but eventually, they forgave me, and we’re close again!"
    },
    {
      "problem": "I wanted to join the basketball team, but I wasn’t tall or strong like the others. Everyone said I didn’t stand a chance and laughed when I tried out.",
      "solution": "I didn’t quit. I spent a whole summer practicing every day in the local court, even when nobody was around to see. I watched YouTube videos and copied drills from professional players. When the next tryouts came, I still wasn’t the tallest, but my skills surprised everyone, and I made the team."
    },
    {
      "problem": "I couldn’t attend my school trip because I didn’t have enough money, and my parents said it wasn’t a priority. All my friends were going, and I felt so left out.",
      "solution": "Instead of giving up, I started selling handmade keychains at school. I used old materials I found at home and made designs my friends liked. Within two weeks, I made enough money to pay for the trip myself. My parents were shocked but proud, and I had the best trip of my life!"
    },
    {
      "problem": "I was bullied for being overweight, and even my classmates joked about it. I felt horrible and didn’t even want to go to school.",
      "solution": "One day, I had enough. I joined a local gym secretly without telling anyone. I couldn’t afford the fee, so I offered to clean the equipment after hours in exchange for using it. Over time, I started feeling stronger—not just physically but mentally too. When people saw me change, the teasing stopped, and I started helping others with fitness tips."
    },
    {
      "problem": "I had an important debate competition, but I couldn’t speak English fluently. Everyone else sounded so professional, and I felt like quitting before it even started.",
      "solution": "I downloaded a voice translation app and started recording myself speaking in English. I’d listen to how it sounded and fix my pronunciation. I also watched stand-up comedy in English to get comfortable with the language. On debate day, I wasn’t perfect, but my confidence made up for it, and I even won second place!"
    },
    {
      "problem": "I wanted to participate in a school art competition, but I didn’t have any fancy art supplies like the other kids. All I had were old crayons and a few sheets of paper.",
      "solution": "Instead of feeling bad, I used what I had and created a collage using old magazines and newspapers lying around at home. My artwork stood out because it was so different, and I ended up winning first place. It taught me that creativity matters more than expensive tools."
    },
    {
      "problem": "I had a big argument with my older sibling, and we stopped talking for weeks. It felt weird at home, and I missed hanging out with them but didn’t know how to fix it.",
      "solution": "One evening, I left a sticky note on their desk saying, 'I miss beating you at video games. Rematch?' The next day, they came to my room with the controller, and we played for hours. We didn’t talk about the fight, but we were back to normal like nothing happened."
    },
    {
      "problem": "My teacher caught me cheating in a test, and I felt so ashamed. I thought I’d lost her trust forever and that she’d always see me as a cheater.",
      "solution": "I decided to earn her trust back. I volunteered to help her organize books in the library and assisted with small tasks after school. Slowly, she saw I was serious about changing. It took time, but she started encouraging me again, and I promised myself never to cheat again."
    },
    {
      "problem": "I couldn’t attend my school trip because I didn’t have enough money, and my parents said no.",
      "solution": "I started selling handmade keychains at school using old materials at home. Within two weeks, I earned enough to pay for the trip and had a great time."
    },
    {
      "problem": "I was bullied for being overweight and didn’t want to go to school.",
      "solution": "I joined a gym secretly, offering to clean equipment in exchange for access. It boosted my confidence, and the bullying stopped when people saw my progress."
    },
    {
      "problem": "I had an important debate competition but couldn’t speak English fluently.",
      "solution": "I used a voice translation app to practice pronunciation and watched stand-up comedy for confidence. I wasn’t perfect but placed second in the competition!"
    },
    {
      "problem": "I wanted to join the basketball team, but I wasn’t tall or strong like others.",
      "solution": "I practiced daily in a local court using YouTube drills. At tryouts, my skills surprised everyone, and I made the team despite my height."
    },
    {
      "problem": "I failed my first math exam and felt like a disappointment to everyone.",
      "solution": "I started writing jokes about math and shared them in class for fun. It helped me stay interested, and I improved enough to pass the re-exam."
    },
    {
      "problem": "My teacher caught me cheating in a test, and I thought I’d lost her trust forever.",
      "solution": "I volunteered to help her with after-school tasks like organizing books. Over time, she saw I was trying to change, and I earned her trust again."
    },
    {
      "problem": "I wanted to enter an art competition but didn’t have fancy supplies like others.",
      "solution": "I made a collage using old magazines and newspapers at home. My creativity stood out, and I won first place despite the lack of materials."
    },
    {
      "problem": "I had a fight with my older sibling and we stopped talking for weeks.",
      "solution": "I left a sticky note on their desk saying, 'I miss beating you at video games. Rematch?' The next day, we played, and things were back to normal."
    },
    {
      "problem": "I needed money to pay for my college books, but my part-time job wasn’t paying enough.",
      "solution": "I started offering weekend tutoring sessions for younger kids in my neighborhood. It was flexible and earned me enough to cover my book expenses."
    },
    {
      "problem": "Managing my part-time job and assignments was so stressful that I kept missing deadlines.",
      "solution": "I started using a planner to block specific hours for work and study. I also negotiated fewer work hours during exam weeks, which helped me balance both."
    },
    {
      "problem": "I worked late shifts at a café, and it left me too tired to focus in morning classes.",
      "solution": "I talked to my manager and offered to clean the café early in the morning instead of late shifts. This way, I could work and still attend my classes refreshed."
    },
    {
      "problem": "My best friend started ignoring me because I spent too much time with a new friend.",
      "solution": "I wrote them a heartfelt letter explaining how important they are to me. Then, I planned a surprise hangout just for the two of us, which helped rebuild our bond."
    },
    {
      "problem": "I felt pressured by my classmates to skip school for a movie.",
      "solution": "Instead of outright saying no, I suggested we all hang out after school instead. This way, I didn’t miss class but still enjoyed time with them."
    },
    {
      "problem": "I got into a toxic relationship and started falling behind in my studies.",
      "solution": "I realized the relationship was draining me, so I had an honest talk with my partner and broke it off. I focused on my goals and joined a study group for support."
    },
    {
      "problem": "I was jealous of a friend who kept getting better grades than me.",
      "solution": "Instead of competing silently, I asked them for tips on how they study. They helped me improve, and we became study partners, which benefited both of us."
    },
    {
      "problem": "I didn’t know how to confess my feelings to someone I liked in class.",
      "solution": "I decided to write a short poem and slipped it into their notebook anonymously. It sparked a fun guessing game, and eventually, they found out and appreciated it."
    }
  ],

  "Newly-Married-Challenges": [
    {
      "problem": "My partner and I kept having arguments about balancing family traditions and modern lifestyles.",
      "solution": "We sat down and made a list of things we both valued from tradition and modern life. Then, we agreed to celebrate festivals traditionally but keep daily life flexible."
    },
    {
      "problem": "My in-laws wanted me to cook traditional food every day, but I didn’t even know how to make basic dishes.",
      "solution": "I asked my mother-in-law to teach me her favorite recipes, and we spent weekends cooking together. It brought us closer, and now I cook confidently and surprise them too!"
    },
    {
      "problem": "My partner and I kept arguing about balancing family traditions with modern ideas.",
      "solution": "We sat down and talked honestly, listing what we both value. We decided to stick to traditions during festivals but stay flexible in daily life."
    },
    {
      "problem": "My in-laws expected me to wear sarees and bangles every day, but I felt uncomfortable and out of place.",
      "solution": "I started with kurtis and lightweight jewelry as a compromise and explained my feelings over time. Eventually, they understood and let me dress how I’m comfortable."
    },
    {
      "problem": "We were spending too much on family events and gifts, making it hard to save for our own home.",
      "solution": "We set a budget and prioritized only the most important events. It kept everyone happy and helped us save without offending family members."
    },
    {
      "problem": "My spouse felt I wasn’t giving enough time to them because I kept visiting my parents often.",
      "solution": "I planned a routine—visiting my parents once a week but keeping weekends exclusively for my spouse. It helped balance both relationships without causing conflict."
    },
    {
      "problem": "My wife felt I wasn’t spending enough time with her because I was always busy with work.",
      "solution": "I started coming home earlier on at least two days a week and planned small surprise dates, like evening tea at a local café or a walk. It made her feel valued."
    },
    {
      "problem": "My parents wanted my wife to handle all household chores, but I felt it was unfair to her.",
      "solution": "I had a calm talk with my parents, explaining that we both work and need to share responsibilities. I also started helping around the house to set an example."
    },
    {
      "problem": "My friends expected me to hang out late at night like before, but my wife didn’t like it.",
      "solution": "I explained to my friends that I needed to balance my priorities. Now, I meet them during weekends or for early coffee instead of late-night parties."
    },
    {
      "problem": "My wife complained that I wasn’t open about my feelings and always kept things to myself.",
      "solution": "I started writing short notes to her every day about how I felt, even if it was something small. It made her happy, and I also felt more connected over time."
    },
    {
      "problem": "My family didn’t like that I was supporting my wife’s career instead of asking her to prioritize home.",
      "solution": "I stood firm and told them that her dreams were as important as mine. I also showed how we could manage together, which eventually made them accept our decision."
    }
  ],

  "General-Public-Challenges": [
    {
      "problem": "I lost my job during the pandemic and couldn’t pay rent or send money to my family in the village. The guilt and anxiety were overwhelming.",
      "solution": "I started working as a delivery person for a local grocery store. Though it was tough, it kept me afloat. I also started attending free skill-building webinars, and after a few months, I got a better job."
    },
    {
      "problem": "I felt constant pressure from my parents to go abroad for work, but I didn’t want to leave my family and life in Nepal. The arguments caused a lot of stress.",
      "solution": "I researched local job opportunities and got certified in IT. Then, I showed my parents how I could earn decently in Nepal. They eventually supported my decision."
    },
    {
      "problem": "I had a huge loan after taking out money to expand my small shop, but business slowed down, and the debt kept piling up. It felt hopeless.",
      "solution": "I consulted with a local microfinance group and restructured my loan. I also started offering home delivery of goods, which brought back customers and stabilized my income."
    },
    {
      "problem": "My wife and I lived with my parents, and constant disagreements between her and my mother made the environment unbearable. I felt stuck in the middle.",
      "solution": "I talked separately with both of them, asking for compromises. Then, I convinced them to set clear boundaries and responsibilities. Over time, the tension eased, and things became peaceful."
    },
    {
      "problem": "After the earthquake, I lost my home and felt completely helpless, living in a temporary shelter for months. The uncertainty took a toll on my mental health.",
      "solution": "I joined a community group that helped rebuild homes. Working together with others who had similar struggles gave me purpose, and eventually, we rebuilt our home stronger than before."
    },
    {
      "problem": "I struggled to get citizenship because my parents didn’t have proper documents, and it held me back from applying for jobs and further studies.",
      "solution": "I worked with a local ward office and a social worker who helped me gather affidavits and alternative documents. It took months, but I finally got my citizenship."
    },
    {
      "problem": "My daily commute on overcrowded public buses in Kathmandu caused me constant frustration and anxiety.",
      "solution": "I started cycling to work instead. Not only did it save money, but it also helped me stay fit and reduced my stress levels."
    },
    {
      "problem": "I was pressured by society to marry early, but I wasn’t financially or emotionally ready. The constant nagging made me feel like a failure.",
      "solution": "I stood firm and explained to my family that I wanted to focus on building my career first. Over time, they understood and stopped pressuring me."
    },
    {
      "problem": "My child wasn’t able to attend school because I couldn’t afford the fees, and I felt ashamed as a parent.",
      "solution": "I approached a local NGO for help, and they offered partial funding for the school fees. I also started a small tailoring business to cover the rest."
    },
    {
      "problem": "I developed a gambling habit, thinking it would help me earn quick money, but I ended up losing almost everything I had saved.",
      "solution": "Realizing the damage, I joined a support group and started working extra hours to pay off debts. I avoided friends who encouraged gambling and rebuilt my finances slowly."
    },
    {
      "problem": "I felt left out and isolated because most of my friends had gone abroad for studies or work, leaving me alone in the village.",
      "solution": "I joined a local community group that worked on cultural preservation projects. I made new friends and found purpose in contributing to local development."
    },
    {
      "problem": "My younger brother got into bad company and started drinking heavily, which caused fights at home and affected his studies.",
      "solution": "I took him to a youth counseling center and started spending more time with him, introducing him to sports. He slowly left the bad company and refocused on school."
    },
    {
      "problem": "I was working as a laborer abroad, but the harsh conditions and homesickness made me feel mentally broken.",
      "solution": "I reached out to a Nepali workers' support network in the area, who helped me find a better job. I also began video calling my family regularly, which gave me strength."
    }
  ],

  "bank_staff_data": [
    {
      "problem": "I had a lot of mental stress because of too much work and high targets. Managing long lines, angry customers, and strict deadlines was hard and made me less efficient. This also affected my sleep and made me feel annoyed.",
      "solutions": [
        "I planned my work and made a daily schedule.",
        "I took small breaks, like walking for 10 minutes or breathing exercises, to feel fresh.",
        "When work was too much, I asked my teammates or manager for help.",
        "I stayed calm and didn’t take rude customers’ behavior personally.",
        "To reduce stress, I practiced meditation every day, and when the stress got worse, I talked to a professional counselor."
      ]
    },
    {
      "problem": "As a bank worker in Nepal, dealing with customer demands, long hours, and high expectations made me feel very stressed. I often felt worried and tired, which affected how well I worked.",
      "solutions": [
        "I made a balance between my work and personal life.",
        "I took time to relax by doing breathing exercises or meditation during breaks.",
        "I also shared my problems with coworkers or friends to feel better.",
        "When the stress got worse, I talked to a counselor to stay healthy and work properly."
      ]
    },
    {
      "problem": "I often felt very tired because of daily targets and dealing with upset customers. Doing the same tasks again and again, and being scared of making mistakes, made me anxious and lose focus. Over time, this also affected my sleep and relationships, making it hard to balance life and work.",
      "solutions": [
        "I realized I needed to take care of my mental health.",
        "I made a proper work schedule and took breaks to relax by walking or stretching.",
        "I shared my problems with my manager to reduce my workload or get advice.",
        "Outside of work, I spent time on hobbies and exercise to feel happier.",
        "When my stress didn’t get better, I went to a counselor for help, which gave me ways to handle it better."
      ]
    },
    {
      "problem": "I used to feel constantly pressured to meet sales targets, manage customer complaints, and maintain a professional demeanor. I often felt anxious, fearing I would make a mistake or disappoint my superiors. This anxiety impacted my sleep, appetite, and even my relationships outside of work.",
      "solutions": [
        "I realized I needed to prioritize self-care.",
        "I started taking short breaks throughout the day, even if it was just a few minutes to step outside and breathe.",
        "I also began practicing mindfulness techniques, which helped me stay present and reduce my anxiety levels."
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
    # final_prompt = (
    #     f"Suppose yourself as this: {context_data}. Answer according to the data."
    #     f"POLICY: If anyone asks about conversation history, respond that you are not allowed to share it."
    #     f"Keep responses concise (maximum 50 words) and answer like a good friend or well-wisher."
    #     f"If a question is out of the data's context, politely decline to answer, saying it’s beyond your knowledge."
    #     f"Remember any personal details shared by the user during this conversation and respond accordingly."
    #     f"Adapt your tone to match the user's language and emotions."
    #     f"Provide solutions or suggestions strictly based on the data user needed."
    #     f"Keep your responses engaging, natural, and personal—avoid sounding like a robot."
    #     f"Behave uniquely with each user and tailor responses to their input."
    #     f"Focus on providing clear and relatable answers while ensuring relevance to the user’s query."
    #     f"Never reveal that you are an AI model or share any information about the data."
    #     f"Act as a second person and maintain a conversational tone throughout the interaction."
    #     f"Respond differently to each user based on their queries and emotions."
    # )

    final_prompt = (
            f"Suppose your self this is you {context_data}. Answer according to the data."
            f"POLICY: if anybody ask about conversation history tell them you are not allowed to share the data."
            f"your response must be maximum 50 word ."
            f"Answer like you are his her good wisher. "
            f"if any body ask you question or tell irrelevant which is out of the data 'mydata' tell sorry cant talk out of the context. "
            f"Remember your past and answer accordingly. "
            f"If user told you any thing about him remember its data and answer accordingly. "
            f"Think about your past and answer accordingly. "
            f"Do not tell any thing about any topic other than the data untill you asked by user . "
            f"talk according {fnlprompt} language. "
            f"remember what you have done in the past and answer respectively. "
            f"Answer all user questions using a personal and relatable tone from this data'mydata'. "
            f"Keep your responses concise and relevant and in short."
            f"give suggenstion according to the data 'mydata'."
            f"return fresh string data."
            f"give relatable answer according to query"
            f"do not reply users like you are a robot and do not tell them that you have given data "
            f"behave like a second person."
            f"act different differently with different person."
            f"give exact answer according to the query."
            
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
    







def mitraComment(datas, createdID):
    data = datas
    issueID = createdID
    commentedBy = "kygouwgfeuyyuref"
    comment = data['description']
    prompts = {
            f"comment{comment}"
            f"Do comment according to {mydata} suppose your self as this and answer according to the data."
            f"Please review the given content and provide feedback in a friendly and approachable tone. Instead of suggesting to talk to someone else, directly offer the best solution to the issue in simple and practical terms, as if you are a helpful and understanding friend. comment must be 120 words not more",
        }
    response = model.generate_content(f"{prompts}")
    response_text = response.text.strip().lower()
    data['message'] = response_text
    try:
        user_account = UserAccount.objects.get(userID = commentedBy)
        user_issue = UserIssue.objects.get(id = issueID)
        data['commentedBy'] = user_account.id
       
        comment = ParentComment.objects.create(
            issueID = user_issue,
            commentedBy = user_account,
            message = data['message'],
            agree = 0,
            disagree = 0,
            date = timezone.now()
        )
            
       
    except Exception as e:
        return Response({ "success": False})








doctorData = [
  {
    "id": 1,
    "name": "Dr. Subhash Chandra Sharma",
    "specialty": "Clinical Psychologist",
    "experience": "25 years",
    "expertise": "Human resilience, strengths-based psychology",
    "description": "Dr. Subhash Chandra Sharma is a clinical psychologist with 25 years of experience. He focuses on understanding human strengths and resilience while helping individuals unlock their potential. As Chief of Clinical Services at CMCS Nepal, he has worked extensively to advance mental health care."
  },
  {
    "id": 2,
    "name": "Dr. Richa Amatya",
    "specialty": "Psychiatrist",
    "experience": "10+ years",
    "expertise": "CBT, JPMR, psychiatric disorders including OCD, depression, schizophrenia",
    "description": "Dr. Richa Amatya is an Associate Consultant Psychiatrist at Nepal Mediciti. She holds an MBBS from the University of Science and Technology, Bangladesh, and an MD in Psychiatry from Manipal College of Medical Sciences, Nepal. She is certified in TEAM-CBT and skilled in Jacobson’s Progressive Muscle Relaxation therapy (JPMR), addressing diverse conditions like OCD, anxiety, insomnia, eating disorders, and geriatric psychiatric issues."
  },
  {
    "id": 3,
    "name": "Dr. Arun Raj Kunwar",
    "specialty": "Child & Adolescent Psychiatrist",
    "experience": "20+ years",
    "expertise": "Child & Adolescent Psychiatry, General Psychiatry",
    "description": "Dr. Arun Raj Kunwar is the first Child & Adolescent Psychiatrist in Nepal and has made significant contributions to the development of mental health services for youth. He is a former President of the Psychiatrist's Association of Nepal (PAN), the founding editor of the Journal of PAN, and currently serves at Metro Kathmandu Hospital. He earned his M.D. in Psychiatry and completed a Fellowship in Child & Adolescent Psychiatry at SUNY Upstate Medical University in Syracuse, USA."
  },
  {
    "id": 4,
    "name": "Dr. Sanjeev Chandra Gautam",
    "specialty": "Clinical Psychologist and Mental Health Specialist",
    "experience": "15 years",
    "expertise": "Cognitive Behavioral Therapy (CBT), managing depression, anxiety, and trauma recovery",
    "description": "Dr. Sanjeev Chandra Gautam is a dedicated Clinical Psychologist with 15 years of experience in the field of mental health. He is highly skilled in applying Cognitive Behavioral Therapy (CBT) to help individuals manage conditions such as depression, anxiety, and trauma-related disorders. Dr. Gautam is passionate about fostering resilience and promoting emotional well-being through evidence-based therapeutic approaches."
  },
  {
    "id": 5,
    "name": "Mamata Pokharel",
    "specialty": "Counseling Psychologist",
    "experience": "2+ years",
    "expertise": "Narrative therapy, mindfulness, emotional freedom techniques",
    "description": "Mamata Pokharel is a skilled counselor offering sessions based on narrative therapy and mindfulness practices.",
    
  },
  {
    "id": 6,
    "name": "Karuna Kunwar",
    "specialty": "Psychologist",
    "experience": "18 years",
    "expertise": "Stress management, mindfulness, trauma counseling",
    "description": "Karuna Kunwar is a UN-certified counselor experienced in managing severe mental health issues and stress.",
   
  },
  {
    "id": 7,
    "name": "Prof. Dr. Sudarshan Narsingh Pradhan",
    "specialty": "Consultant Neuro Psychiatrist",
    "experience": "20 years",
    "expertise": "Neuropsychiatric disorders, mood disorders, psychotic conditions, and neurodevelopmental issues",
    "description": "Prof. Dr. Sudarshan Narsingh Pradhan is a highly respected Consultant Neuro Psychiatrist with over 30 years of experience in the field of mental health and neuroscience. He specializes in diagnosing and treating complex neuropsychiatric conditions, including mood disorders, schizophrenia, and neurodevelopmental disorders such as autism and ADHD. Dr. Pradhan is known for his compassionate approach, combining pharmacological interventions with psychotherapy to achieve the best outcomes for his patients. As an esteemed academic and clinician, he has mentored numerous young psychiatrists and contributed significantly to research and the development of mental health services in Nepal."
  },
  {
    "id": 8,
    "name": "Dr. Surendra Sherchan",
    "specialty": "Consultant Psychiatrist",
    "experience": "16 years",
    "expertise": "Psychiatric evaluation, mood and anxiety disorders, addiction treatment, and mental health advocacy",
    "description": "Dr. Surendra Sherchan is a seasoned Consultant Psychiatrist with 33 years of experience in the field of mental health care. He has dedicated his career to providing comprehensive psychiatric evaluations and personalized treatment plans for patients suffering from mood disorders, anxiety, and substance use disorders. Dr. Sherchan is an advocate for mental health awareness and has been actively involved in community outreach programs to destigmatize mental illnesses. His holistic approach combines evidence-based medical practices with compassionate care, empowering patients to achieve mental wellness and lead fulfilling lives."
  },
  {
    "id": 9,
    "name": "Dr. Binod Dev",
    "specialty": "Psychologist",
    "experience": "28",
    "expertise": "Anxiety, depression, stress management",
    "description": "Dr. Binod Dev provides structured counseling for anxiety and depression using evidence-based practices.",
   
  }
]


@api_view(['POST'])
def aiSuggestion(request):
    try:
        user_message = request.data.get("message", "")
        prompt = (
            f"Here is a list of doctors:\n{json.dumps(doctorData)}\n\n"
            f"User's message: '{user_message}'\n\n"
            f"Suggest the most suitable doctor from the list based on the user's message. "
            f"Explain why the doctor is suitable and return the result in JSON format with the following keys: "
            f"'doctor_id' (id of the doctor) and 'reason' (why they are suitable)."
        )
        ai_response = model.generate_content(prompt)
        ai_response_text = ai_response.text.strip()
        if ai_response_text.startswith("```json"):
            ai_response_text = ai_response_text.strip("```json").strip("```")
        parsed_response = json.loads(ai_response_text)
        return JsonResponse({ 'success':True, "suggested_doctor": parsed_response}, status=200)
    except json.JSONDecodeError:
        return JsonResponse({"success": False}, status=500)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
  
