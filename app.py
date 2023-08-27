from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Load conversation data from JSON file
def load_conversation_data():
    with open("conversation.json", "r") as json_file:
        conversation_data = json.load(json_file)
    return conversation_data

@app.route("/", methods=["GET", "POST"])
def chatbot():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        response = chatbot_response(user_input)
        return render_template("index.html", user_input=user_input, chatbot_response=response)

    return render_template("index.html", user_input="", chatbot_response="")

def chatbot_response(query):
    conversation_data = load_conversation_data()

    # Access the "queries" array from conversation_data
    queries = conversation_data["queries"]

    # Iterate through individual query-response pairs
    for item in queries:
        if query.lower() in item["query"].lower():
            return item["response"]
    
    return "I'm sorry, I don't have a response for that query."

if __name__ == "__main__":
    app.run(debug=True)
