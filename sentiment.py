import tensorflow as tf
from transformers import (
    TFBertModel,
    BertTokenizer,
    TFAutoModelForSequenceClassification,
    DataCollatorWithPadding,
    pipeline,
)

tokenizer_h = BertTokenizer.from_pretrained("Guspfc/my-awesome-bert-model-hate-speech")
model_h = TFAutoModelForSequenceClassification.from_pretrained(
    "Guspfc/my-awesome-bert-model-hate-speech"
)


class SentimentAnalyzer:
    sentiment_model: str = "Guspfc/my-awesome-bert-model-sentiment-analysis"
    hate_speech_model: str = "Guspfc/my-awesome-bert-model-hate-speech"

    # Initialize Bert Model and Tokenizer
    def __init__(self) -> None:
        self.tokenizer_sentiment = BertTokenizer.from_pretrained(self.sentiment_model)
        self.model_sentiment = TFAutoModelForSequenceClassification.from_pretrained(
            self.sentiment_model
        )

        self.tokenizer_hate = BertTokenizer.from_pretrained(self.hate_speech_model)
        self.model_hate = TFAutoModelForSequenceClassification.from_pretrained(
            self.hate_speech_model
        )

    # Method to Analyse sentiment of text
    def analyze_sentiment(self, text: str):
        input_token = self.tokenizer_sentiment(text, return_tensors="tf")

        outputs = self.model(**input_token)
        logits = outputs.logits

        probabilities = tf.nn.softmax(logits, axis=-1)

        predicted_class = tf.argmax(probabilities, axis=1).numpy()[0]

        if predicted_class == 1:
            return "Neutral 😐"
        elif predicted_class == 2:
            return "Negative ❌"
        else:
            return "Positive ✅"

    # Method to Analyse Hate Speech in text
    def analyze_hate_speech(self, text: str):
        input_token = self.tokenizer_hate(text, return_tensors="tf")

        outputs = self.model(**input_token)
        logits = outputs.logits

        probabilities = tf.nn.softmax(logits, axis=-1)

        predicted_class = tf.argmax(probabilities, axis=1).numpy()[0]

        if predicted_class == 0:
            return "Hate Speech Detected ☠️"
        elif predicted_class == 1:
            return "Offensive Language Detected 🤬"
        else:
            return None
