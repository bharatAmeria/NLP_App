import paralleldots

class API:

    def __int__(self):
        paralleldots.set_api_key("Your_API_ key")

    def sentiment_analysis(self, text):
        response = paralleldots.sentiment(text)
        return response

    def ner(self, text):
        paralleldots.ner(text)

    def emotion_prediction(self, text):
        paralleldots.emotion(text)

