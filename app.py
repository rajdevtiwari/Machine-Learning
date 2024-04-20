import pickle
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import uuid
import numpy as np

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['ticket_resolution']
complaints_collection = db['complaints']
# Load the pre-trained model
with open('model.pkl', 'rb') as f:
    tfidf_vectorizer, classifier = pickle.load(f)

# Define route for the index page
@app.route('/')
def index():
    return render_template('index.html')

# Define route for classifying the complaint
@app.route('/classify', methods=['POST'])
def classify_complaint():
    complaint = request.form['complaint']
    print(complaint)
    tcomplaint=tfidf_vectorizer.transform([complaint])
    print(tcomplaint)
    pdepartment = classifier.predict(tcomplaint)
    print(pdepartment[0])
    ppdepartment=pdepartment[0]
    # Generate ticket number
    ticket_no = str(uuid.uuid4())[:8]

    # Save complaint in MongoDB
    complaints_collection.insert_one({
        'ticket_no': ticket_no,
        'complaint_text': complaint,
        'department': ppdepartment
    })

    # Return response to frontend
    return jsonify({
        'TicketNo': ticket_no,
        'Department': ppdepartment
    })    
    #return render_template('index.html', department=department)

if __name__ == '__main__':
    app.run(host="192.168.1.65",port=5000,debug=True)
