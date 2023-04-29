import openai
class Chatbot:
    def __init__(self):
        openai.api_key="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"
    
    def get_response(self, user_input):
        response=openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return response

if __name__=="__main__":
    chatbot=Chatbot()
    response=chatbot.get_response("")
    print(response)