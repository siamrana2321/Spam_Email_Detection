from flask import Flask, render_template, request, jsonify
import joblib
import string
from nltk.corpus import stopwords

app = Flask(__name__)

# Load the model and vectorizer
model = joblib.load('spam_classifier_model.pkl')
vectorizer = joblib.load('count_vectorizer.pkl')

# Preprocess text function
def preprocess_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    text = ' '.join([word for word in text.split() if word not in stopwords.words('english')])
    return text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            if 'message' not in request.form:
                return jsonify({'error': 'No message provided'}), 400

            message = request.form['message']
            cleaned_message = preprocess_text(message)
            vectorized_message = vectorizer.transform([cleaned_message]).toarray()
            prediction = model.predict(vectorized_message)
            result = 'Spam' if prediction[0] == 1 else 'Ham'
            return render_template('index.html', result=result, email=message)
        except Exception as e:
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)