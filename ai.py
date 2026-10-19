from openai import OpenAI
import json
import os

client = OpenAI(
       api_key=os.environ["GEMINI_API_KEY"],
       base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
   )

def analyze_resume(resume_text, user_goal):
    prompt = f"""
you are a senior software engineer and hiring manager,

Evaluate the resume based on the user;s goal.OpenAI

User goal: "{user_goal}"OpenAI

STRICT RULES:
- Extract only relevant skills for this goal
- REMOVE irrelevant tools [excel for backend, etc]
- Identify real gaps
- Generate roadmap only for the missing fields
- Make output DIFFERENT  based on goal

Return only JSON:
{{

"Skills":[],
"missing skills":[],
"roadmap":[],
"interview_questions":[]

}}
Resume :
{resume_text}
"""
    try:
        response= client.chat.completions.create(
            model="gemini-3.5-flash",
            temperature = 0.3,
            messages=[
                {"role": "system", "content":"You are a strict hiring manager."},
                {"role": "user", "content":prompt}
            ]
        )

        content = response.choices[0].message.content.strip()

        start = content.find("{")
        end = content.rfind("}") + 1
        
        return json.loads(content[start:end])
    except Exception as e:
        return{
            "skills":[],
            "missing_skills":[],
            "roadmap":[],
            "interview_questions":[],
            "error":str(e)
        }

