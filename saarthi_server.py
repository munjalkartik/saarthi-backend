from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/')
def home():
    return '✅ Saarthi AI backend is live'

@app.route('/ask', methods=['GET'])
def ask():
    query = request.args.get('query')
    if not query:
        return jsonify({'response': '❌ No query received'}), 400

    try:
        # Send query to ChatGPT
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert on Bhagavad Gita. Give answers in Hindi shloka, Hindi meaning, English meaning, and Hinglish meaning."},
                {"role": "user", "content": query}
            ],
            temperature=0.7,
            max_tokens=500
        )
        reply = response['choices'][0]['message']['content']
        return jsonify({'response': reply})

    except Exception as e:
        return jsonify({'response': f'❌ Error: {str(e)}'}), 500
