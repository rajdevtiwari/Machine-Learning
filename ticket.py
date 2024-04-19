# Importing necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
import pickle

# Sample dataset related to society maintenance services
data = {
    'ticket_text': [
        "The elevator is not working",
        "There is a leak in the roof",
        "The hallway lights are flickering",
        "The swimming pool water is dirty",
        "The gate is damaged and needs repair",
        "There is no water supply in the bathrooms",
        "The garden needs cleaning",
        "The gym equipment needs fixing",
        "There is a pest infestation in the common area",
        "The parking area needs cleaning",
        "The security cameras are not functioning properly",
        "The community hall needs renovation",
        "The playground lights are broken",
        "The fire alarm keeps beeping",
        "There is a strainger romming in club area",
        "The internet connection is slow",
        "The garbage collection schedule needs to be revised",
        "There is a power outage in the building",
        "The mailboxes are jammed",
        "There is a strange odor in the corridor"
    ],
    'department': [
        'Maintenance',
        'Maintenance',
        'Electricity',
        'House Keeping',
        'Maintenance',
        'Plumbing',
        'House Keeping',
        'Maintenance',
        'House Keeping',
        'House Keeping',
        'Security',
        'Maintenence',
        'Electricity',
        'Maintenence',
        'Security',
        'Electricity',
        'House Keeping',
        'Electricity',
        'House Keeping',
        'House Keeping'
    ]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['ticket_text'], df['department'], test_size=0.2, random_state=0)

# Creating TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fitting the vectorizer and transforming the training data
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)

# Transforming the testing data
X_test_tfidf = tfidf_vectorizer.transform(X_test)

# Training a Linear Support Vector Classifier
classifier = LinearSVC()
classifier.fit(X_train_tfidf, y_train)

# Making predictions on the testing data
predictions = classifier.predict(X_test_tfidf)

# Evaluating the model
print(classification_report(y_test, predictions))

# Example usage
def tag_ticket(text):
    text_tfidf = tfidf_vectorizer.transform([text])
    print(text_tfidf)
    prediction = classifier.predict(text_tfidf)
    return prediction[0]

# Testing the tag_ticket function
ticket_text = "The elevator is not working"
predicted_department = tag_ticket(ticket_text)
print(f"The predicted department for the ticket '{ticket_text}' is: {predicted_department}")

# Dumping the trained model into a pickle file
with open('model.pkl', 'wb') as f:
    pickle.dump((tfidf_vectorizer, classifier), f)