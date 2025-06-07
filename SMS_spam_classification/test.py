import pickle

# Load model and vectorizer
model = pickle.load(open("spam_classifier_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

# Example usage
msg = ["Hello! Are we meeting today at 5?"]
vec = vectorizer.transform(msg)
result = model.predict(vec)

print("Spam" if result[0] else "Ham")
