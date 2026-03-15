from dotenv import load_dotenv
from fastapi import FastAPI ,HTTPException
from google import genai
from google.genai import types
from models import ChatResponse, ChatRequest

load_dotenv()
client = genai.Client()

app = FastAPI(
    title="My FastAPI Application",
)

@app.post(
    path="/chat",
    response_model=ChatResponse,
    summary="Gemini API'sine bir mesaj gönderir ve yanıt alır",
)

async def generate_chat(request:ChatRequest):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents= request.message,
        )
        config = types.GenerateContentConfig(system_instruction=request.system_prompt,
                                             temperature= request.temperature)
        return ChatResponse(result =response.text)

    except Exception as e:
        raise HTTPException(str(e))

# @app.get('/check')
# def deneme():
#     return{'result': 'success'}
