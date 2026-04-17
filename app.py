from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_input = request.json.get("message", "").strip()

        if not user_input:
            return jsonify({"response": "Please enter a message."})

        response = get_response(user_input)

        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"response": "Something went wrong. Please try again."})


if __name__ == "__main__":
    print("Server running at: http://127.0.0.1:5000/")
    app.run(debug=True, use_reloader=False)