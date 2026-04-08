from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = [
    "I love this", "This is amazing", "Very happy",
    "I hate this", "This is bad", "Very sad"
]

labels = ["positive", "positive", "positive",
          "negative", "negative", "negative"]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

def predict_sentiment(text):
    x = vectorizer.transform([text])
    return model.predict(x)[0]
