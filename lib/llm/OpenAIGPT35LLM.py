from time import sleep
import openai
from os import getenv
from lib.logger import debug
from lib.llm.BaseLLM import BaseLLM, BaseMessage, ROLE_USER, ROLE_ASSISTANT, ROLE_SYSTEM
import lib.const as const

class OpenAIGPT35LLM(BaseLLM):

    def __init__(self, *args, **kwargs):        

        super().__init__(*args, **kwargs)

        self.args["api_key"] = kwargs.get("api_key", getenv("OPENAI_API_KEY"))
        self.args["model"] = kwargs.get("model", "gpt-3.5-turbo-0125")

        self.client = openai.OpenAI();
    

    def text_to_text_completion( self, text ):
        debug( type(self).__name__, "text_to_text_completion() :: Luodaan vastaus" )
        
        if const.DO_FAKE_LLM:
            return self._text_to_text_completion_fake( text )

        message = self._chat_completion_single_message( text );
        response = message.content;

        self.message_history.append( BaseMessage( content=response, role=ROLE_ASSISTANT ))

        return response
    

    def _text_to_text_completion_fake( self, text ):

        self._text_to_messages( text )

        sleep(1)

        return super()._text_to_text_completion_fake( text )


    def _chat_completion_single_message( self, text ) -> BaseMessage:
    
        return self._chat_completion_messages( self._text_to_messages( text ))


    def _chat_completion_messages( self, messages ) -> BaseMessage:
    
        completion = self._run_chat_completion( messages )

        result = completion.choices[0].message

        return BaseMessage( content=result.content, role=result.role )
    

    def _run_chat_completion( self, messages ):

        return self.client.chat.completions.create(
            model=self.args["model"],
            messages=messages,
            stream=False,
        )

    def _text_to_messages( self, text ):

        self.message_history.append( BaseMessage( content=text, role=ROLE_USER ))

        messages = []
        for message in self.message_history:
            messages.append( { "role": message.role, "content": message.content } )

        return messages
    

llm = OpenAIGPT35LLM()