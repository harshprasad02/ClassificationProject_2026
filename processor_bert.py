from sentence_transformers import SentenceTransformer
import joblib
# Load the sentence transformer model used for training
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# import os
# print(os.listdir())
# print(os.listdir('Classification_project/models'))
    # Load the trained classifier
classifier = joblib.load('Classification_project/models/log_classifier.joblib')


def classify_with_bert(log_message):
    # Encode the log message to get the embedding
    embedding = embedder.encode([log_message])[0]
    probabilities = classifier.predict_proba([embedding])[0]
    
    if max(probabilities) < 0.5:
        return "Unclassified"
        
    # Predict the label
    prediction = classifier.predict([embedding])[0]
    
    return prediction

if __name__ == "__main__":
    logs = [
        "alpha.osapi_compute.wsgi.server - 12.10.11.1 - API returned 404 not found error",
        "GET /v2/3454/servers/detail HTTP/1.1 RCODE 404 len: 1583 time: 0.1878400",
        "System crashed due to drivers errors when restarting the server",
        "Hey bro, chill ya!",
        "Multiple login failures occurred on user 6454 account",
        "Server A790 was restarted unexpectedly during the process of data transfer"
        ]

    for log in logs:
        
        label = classify_with_bert(log)
        print(log, "->", label)