from flask import Flask, render_template, request, jsonify
import openai
import json

app = Flask(__name__)

# Load conversation data from JSON file
def load_conversation_data():
    with open("conversation.json", "r") as json_file:
        conversation_data = json.load(json_file)
    return conversation_data

# Configure OpenAI API key
openai.api_key = "YOUR_GPT3_API_KEY"

@app.route("/", methods=["GET", "POST"])
def chatbot():
    if request.method == "POST":
        user_input = request.json.get("user_input")
        response = chatbot_response(user_input)
        return jsonify({"chatbot_response": response})

    return render_template("index.html", chat_history=chat_history)

def chatbot_response(query):
    conversation_data = load_conversation_data()

    # Generate a response using GPT-3
    prompt = f"User: {query}\nChatbot:"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50,
    )

    generated_response = response.choices[0].text.strip()
    chat_history.append({"text": query, "class": "user-message"})
    chat_history.append({"text": generated_response, "class": "bot-message"})
    return generated_response

chat_history = []

if __name__ == "__main__":
    app.run(debug=True)
