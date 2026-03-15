from typing import Optional

from pydantic import BaseModel


class ChatRequest(BaseModel):
    message : str = Field(description="The message to send to the chatbot", example="Hello, how are you?")

    #This code block is used to add the system prompt field to the Chat Request model. It contains the first statement to be passed during Execute.
    system_prompt: Optional[str] = Field(default="The system prompt to use for the chatbot", example="Hello, I'm a helpful assistant. How can I assist you?")
    temperature = Optional[float] =Field(default = 0.7 , ge=0.0 , le = 2.0)

class ChatRsponse(BaseModel):
    result:str    
