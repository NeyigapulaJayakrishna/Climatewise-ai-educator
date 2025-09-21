from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import openai
import os
import json

app = Flask(__name__)

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load quiz data
with open('data/quiz.json', 'r') as f:
    quiz_data = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant educating users on climate change in simple language."},
            {"role": "user", "content": user_input}
        ]
    )
    reply = response.choices[0].message.content
    return jsonify({'reply': reply})

@app.route('/quiz', methods=['GET'])
def quiz():
    return jsonify(quiz_data)

if __name__ == '__main__':
    app.run(debug=True)
