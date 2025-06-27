from fastapi import FastAPI, Request
from backend.agent import chat_with_user

app = FastAPI()

@app.post("/chat/")
async def chat(request: Request):
    data = await request.json()
    user_input = data.get("user_input", "")
    response = chat_with_user(user_input)
    return {"response": response}
