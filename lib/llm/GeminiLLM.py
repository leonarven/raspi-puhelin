from requests import post
from os import getenv
from time import sleep

import lib.const as const
from lib.logger import debug

from .OpenAIGPT35LLM import OpenAIGPT35LLM
from lib.llm.BaseLLM import BaseMessage, ROLE_SYSTEM, ROLE_USER, ROLE_ASSISTANT

class GeminiLLM(OpenAIGPT35LLM):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.roles_mapping[ ROLE_ASSISTANT ] = "model"

        self.args["api_key"] = kwargs.get("api_key", getenv("GOOGLE_API_KEY"))
        self.args["model"]   = kwargs.get("model", "gemini-1.0-pro")

        location   = kwargs.get("location",   getenv("GOOGLE_LOCATION"))
        project_id = kwargs.get("project_id", getenv("GOOGLE_PROJECT_ID"))
        endpoint   = f"{ location }-aiplatform.googleapis.com"

        api_endpoint = f"https://{ endpoint }/v1/projects/{ project_id }/locations/{ location }/publishers/google/models/{ self.args['model'] }:generateContent"

        self.args["api_endpoint"] = api_endpoint
        

    def _chat_completion_messages( self, messages ) -> BaseMessage:
    
        completion = self._run_chat_completion( messages )

        result = completion["candidates"][0]["content"]

        role    = self.decodeRole( result["role"] )
        content = result["parts"][0]["text"] if result["parts"] else ""

        return BaseMessage( content=content, role=role )
    

    def _run_chat_completion( self, messages ):

        contents = []

        for message in messages:
            if message["role"] == ROLE_SYSTEM:
                contents.append({
                    "role": self.encodeRole( ROLE_USER ),
                    "parts": { "text": message["content"] }
                });
                contents.append({
                    "role": self.encodeRole( ROLE_ASSISTANT ),
                    "parts": { "text": "Minä tottelen!" }
                });
            else:
                contents.append({
                    "role": self.encodeRole( message["role"] ),
                    "parts": {
                        "text": message["content"]
                    }
                })
            
        print("contents", contents)

        response = post(
            self.args["api_endpoint"],
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": f"Bearer { self.args['api_key'] }"
            },
            json = {
                "contents": contents,
                "safety_settings": [{
                    "category": "HARM_CATEGORY_HARASSMENT",
                    "threshold": "BLOCK_NONE"
                },{
                    "category": "HARM_CATEGORY_HATE_SPEECH",
                    "threshold": "BLOCK_NONE"
                },{
                    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    "threshold": "BLOCK_NONE"
                },{
                    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                    "threshold": "BLOCK_NONE"
                }]
            }
        )

        response = response.json()
        print( "response",response)
        return response;


llm = GeminiLLM()