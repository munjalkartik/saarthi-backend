from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key from environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/respond", methods=["GET", "POST"])
def respond():
    query = request.args.get("query") or request.json.get("query")

    if not query:
        return jsonify({"response": "❌ No query received"}), 400

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Saarthi, a voice assistant for the Bhagavad Gita. Respond clearly and kindly. Keep the tone friendly."},
                {"role": "user", "content": query}
            ]
        )

        answer = completion.choices[0].message["content"]
        return jsonify({"response": answer})

    except Exception as e:
        return jsonify({"response": f"❌ Error: {str(e)}"}), 500

@app.route("/")
def index():
    return "✅ Saarthi AI backend is live"

if __name__ == "__main__":
    app.run()
