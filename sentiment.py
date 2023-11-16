import tensorflow as tf
from transformers import (
    TFBertModel,
    BertTokenizer,
    TFAutoModelForSequenceClassification,
    DataCollatorWithPadding,
    pipeline,
)

class SentimentAnalyzer:
    bert_model: str = "Guspfc/my-awesome-bert-model-sentiment-analysis"

    # Initialize Bert Model and Tokenizer
    def __init__(self) -> None:
        self.tokenizer = BertTokenizer.from_pretrained(self.bert_model)
        self.model = TFAutoModelForSequenceClassification.from_pretrained(
            self.bert_model
        )

    # Method to Analyse sentiment of text
    def analyze(self, text: str):
        input_token = self.tokenizer(text, return_tensors="tf")

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
